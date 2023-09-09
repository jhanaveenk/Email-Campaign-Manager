from django.db import models

# Database Model for Subscriber
class Subscriber(models.Model):
   email = models.EmailField(unique=True)
   first_name = models.CharField(max_length=50)
   status_tag=models.BooleanField(default=True, editable=False)
   # status_tag = models.CharField(max_length=10, choices=TAG_CHOICES, default=None, editable=False)

   def __str__(self):
      return self.email

## Databse model for the email campaign fields
class EmailCampaign(models.Model):
   subject = models.CharField(max_length=255)
   preview_text = models.TextField()
   article_url = models.URLField()
   html_content = models.TextField()
   plain_text_content = models.TextField()
   published_date = models.DateField()

   def __str__(self):
      return self.subject
