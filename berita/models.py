from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import ImageField
from django.utils import timezone

# Create your models here.

class Berita(models.Model):
    judul = models.CharField(max_length = 255)
    gambar = models.ImageField(max_length = 255, default="")
    isi = models.TextField()
    kontributor = models.CharField(max_length = 255)
    tanggal = models.DateField(default = timezone.now)
    comment = models.CharField(max_length = 25, default="0")
    kategori = models.CharField(max_length = 25, default="berita")

class Ekonomi(models.Model):
    judul = models.CharField(max_length = 255)
    gambar = models.ImageField(max_length = 255, default="")
    isi = models.TextField()
    kontributor = models.CharField(max_length = 255)
    tanggal = models.DateField(default = timezone.now)
    comment = models.CharField(max_length = 25, default="0")
    kategori = models.CharField(max_length = 25, default="ekonomi")

class Otomotif(models.Model):
    judul = models.CharField(max_length = 255)
    gambar = models.ImageField(max_length = 255, default="")
    isi = models.TextField()
    kontributor = models.CharField(max_length = 255)
    tanggal = models.DateField(default = timezone.now)
    comment = models.CharField(max_length = 25, default="0")
    kategori = models.CharField(max_length = 25, default="otomotif")

class OlahRaga(models.Model):
    judul = models.CharField(max_length = 255)
    gambar = models.ImageField(max_length = 255, default="")
    isi = models.TextField()
    kontributor = models.CharField(max_length = 255)
    tanggal = models.DateField(default = timezone.now)
    comment = models.CharField(max_length = 25, default="0")
    kategori = models.CharField(max_length = 25, default="olah raga")

