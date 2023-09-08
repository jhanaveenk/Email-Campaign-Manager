from django.contrib import admin
from .models import Subscriber

# Feilds to display on admin site
class SubscriberAdmin(admin.ModelAdmin):
   list_display = ('email', 'name', 'status_tag')
   search_fields = ('email', 'name',)
   list_filter = ('status_tag',)

# Registered Subscriber model
admin.site.register(Subscriber, SubscriberAdmin)

