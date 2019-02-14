from django.contrib import admin
from django.contrib import admin
from .models import Redaksi

# Register your models here.

my_model = [Redaksi]
admin.site.register(my_model)