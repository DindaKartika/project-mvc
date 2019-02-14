from django.urls import path
from . import views

urlpatterns = [
   path('', views.base, name='base'),
   path('h', views.home, name='home'),
   path('index', views.index, name='index'),
   path('foto', views.foto, name='foto')
]