from django.urls import path
from . import views

urlpatterns =[
   path('api/add_subscriber/', views.add_subscriber, name='add_subscriber'),
   path('api/unsubscribe/<str:email>/', views.unsubscribe, name='unsubscribe'),
   path('api/send_daily_campaign/', views.send_daily_campaign, name='send_daily_campaign'),

]