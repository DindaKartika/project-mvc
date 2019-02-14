from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import ImageField
from django.utils import timezone

# Create your models here.
class Member(models.Model):
    user_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100, default="")
    password = models.CharField(max_length = 25)