from django.urls import path
from . import views

urlpatterns = [
   path('h', views.home, name='home'),
   path('index', views.index, name='index'),
   path('foto', views.foto, name='foto'),
   path('berita/<int:id>', views.hlm_berita, name='hlmberita'),
]
