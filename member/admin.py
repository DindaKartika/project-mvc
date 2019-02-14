from django.contrib import admin
from django.contrib import admin
from .models import Member

# Register your models here.

my_model = [Member]
admin.site.register(my_model)