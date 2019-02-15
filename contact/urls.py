from django.urls import path
from . import views

urlpatterns = [
   path('contact', views.contact, name='contact'),
   path('input_contact/', views.input_contact, name = 'input_contact'),
]