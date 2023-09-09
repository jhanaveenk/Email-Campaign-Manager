from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Subscriber, EmailCampaign
from .serializers import SubscriberSerializer, EmailCampaignSerializer
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from datetime import date
from django.utils.html import strip_tags


# Viewset fuction for getting the list and add new subscriber
@api_view(['GET', 'POST'])
def add_subscriber(request):
   if request.method == 'GET':
      subscribers = Subscriber.objects.all()
      serializer = SubscriberSerializer(subscribers, many=True)
      return Response(serializer.data)
    
   if request.method == 'POST':
      serializer = SubscriberSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Viewset fuction for unsubscribe users
@api_view(['PATCH'])
def unsubscribe(request, email):
   if request.method=='PATCH':
      email = request.data.get('email', None)
      if email is not None:
         try:
            subscriber = Subscriber.objects.get(email=email)
            subscriber.status_tag = False
            subscriber.save()
            return Response({'message': f'{email} unsubscribed successfully.'})
         except Subscriber.DoesNotExist:
            return Response({'error': 'Subscriber not found.'}, status=status.HTTP_404_NOT_FOUND)
      else:
         return Response({"message": "Email field is required"}, status=status.HTTP_400_BAD_REQUEST)


# Viewset fuction for sending daily campaigns to subscribers
@api_view(['POST'])
def send_daily_campaign(request):
    if request.method == 'POST':
      current_date = date.today()
      try:
         campaign = EmailCampaign.objects.get(published_date=current_date)
      except EmailCampaign.DoesNotExist:
         return Response({'message': 'No campaign found for today.'}, status=status.HTTP_404_NOT_FOUND)
      
      subscribers = Subscriber.objects.filter(status_tag=True)
      for subscriber in subscribers:
         send_campaign_email(subscriber.email, campaign)
      return Response({'message': 'Daily campaign emails sent successfully.'}, status=status.HTTP_200_OK)
    

def send_campaign_email(recipient_email, campaign):
   email_content = loader.render_to_string(
      'email_campaign/campaign_email_template.html',
      {
         'subject': campaign.subject,
         'preview_text': campaign.preview_text,
         'article_url': campaign.article_url,
         'published_date': campaign.published_date,
         'html_content': campaign.html_content,
      }
    )
   
   # Created the email message
   message = EmailMultiAlternatives(
      subject=campaign.subject,
      body=strip_tags(email_content),
      from_email=settings.EMAIL_HOST_USER,
      to=[recipient_email],
    )
   message.attach_alternative(email_content, "text/html")
   message.send()
