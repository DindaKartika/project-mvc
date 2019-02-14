from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import ImageField
from django.utils import timezone

# Create your models here.
class Redaksi(models.Model):
    nama = models.CharField(max_length = 255)
    jabatan = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama