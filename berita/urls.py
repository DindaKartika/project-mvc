from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('index', views.index, name='index'),
   path('foto', views.foto, name='foto'),
   path('berita/<int:id>', views.hlm_berita, name='hlm_berita'),
   path('ekonomi/<int:id>', views.hlm_ekonomi, name='hlm_ekonomi'),
   path('olahraga/<int:id>', views.hlm_olahraga, name='hlm_olahraga'),
   path('otomotif/<int:id>', views.hlm_otomotif, name='hlm_otomotif'),
   path('berita/input', views.form_berita, name='form_berita'),
   path('ekonomi/input', views.form_ekonomi, name='form_ekonomi'),
   path('olahraga/input', views.form_olahraga, name='form_olahraga'),
   path('otomotif/input', views.form_otomotif, name='form_otomotif')
]