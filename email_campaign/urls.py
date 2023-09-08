from django.urls import path
from . import views

urlpatterns =[
   path('api/add_subscriber/', views.add_subscriber, name='add_subscriber'),
]