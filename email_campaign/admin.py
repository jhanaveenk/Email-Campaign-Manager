from django.contrib import admin
from .models import Subscriber

# Feilds to display on admin site
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')
    search_fields = ('email', 'name')

# Registered Subscriber model
admin.site.register(Subscriber, SubscriberAdmin)

