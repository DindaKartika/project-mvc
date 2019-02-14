from django.contrib import admin
from django.contrib import admin
from .models import Berita, Ekonomi, Otomotif, OlahRaga
# Register your models here.

my_model = [Berita, Ekonomi, Otomotif, OlahRaga]
admin.site.register(my_model)