from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Subscriber 
from .models import EmailCampaign
from .serializers import EmailCampaignSerializer
from datetime import date
from django.core import mail


## This is a test case for testing the send_daily_campaign() function
class SendDailyCampaignTestCase(TestCase):
  def setUp(self):
    self.campaign = EmailCampaign.objects.create(
      subject='Test Campaign',
      preview_text='This is a test campaign',
      article_url='https://github.com/jhanaveenk',
      published_date=date.today(),
      html_content='<p>This is a HTML content.</p>',
        )

    self.subscriber = Subscriber.objects.create(
        email='jhanaveen255@gmail.com',
        name='Naveen Jha'
        )

    self.client = APIClient()

    def test_send_daily_campaign(self):
      url = reverse('send_daily_campaign')

      response = self.client.post(url, format='json')

      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIn('message', response.data)

      # Checking if the email campaign was sent
      self.assertEqual(len(mail.outbox), 1) 
      sent_email = mail.outbox[0]
      campaign = self.campaign
      # Checking email subject
      self.assertEqual(sent_email.subject, campaign.subject)

      # Check email recipient
      self.assertEqual(sent_email.to, [self.subscriber.email])
   

