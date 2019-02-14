from django.contrib import admin
from django.contrib import admin
from .models import Kategori, Berita
# Register your models here.

my_model = [Kategori, Berita]
admin.site.register(my_model)