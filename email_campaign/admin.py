from django.contrib import admin
from .models import Subscriber, EmailCampaign

# Feilds to display on admin site
class SubscriberAdmin(admin.ModelAdmin):
   
   list_display = ('email', 'first_name', 'status_display')
   search_fields = ('email', 'first_name',)
   list_filter = ('status_tag',)

# Registered Subscriber model
admin.site.register(Subscriber, SubscriberAdmin)

