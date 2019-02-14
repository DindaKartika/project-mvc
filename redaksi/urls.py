from django.urls import path
from . import views

urlpatterns = [
   path('redaksi', views.redaksi, name='redaksi')
]