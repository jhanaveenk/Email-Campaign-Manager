from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Subscriber
from .serializers import SubscriberSerializer

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
    

@api_view(['PATCH'])
def unsubscribe(request, email):
   try:
      subscriber = Subscriber.objects.get(email=email)
      subscriber.status_tag = "inactive"
      subscriber.save()
      return Response({'message': f'{email} unsubscribed successfully.'})
   except Subscriber.DoesNotExist:
      return Response({'error': 'Subscriber not found.'}, status=status.HTTP_404_NOT_FOUND)

