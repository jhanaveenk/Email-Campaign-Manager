from django.db import models



# Database Model for Subscriber
class Subscriber(models.Model):
   email = models.EmailField(unique=True)
   name = models.CharField(max_length=50)
   TAG_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),]
   status_tag = models.CharField(max_length=10, choices=TAG_CHOICES, default=None, editable=False)

   def __str__(self):
      return self.email