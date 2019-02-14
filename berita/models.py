from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import ImageField
from django.utils import timezone

# Create your models here.

class Kategori(models.Model):
    kategori = models.CharField(max_length = 255)

    def __str__(self):
        return self.kategori
        
class Berita(models.Model):
    judul = models.CharField(max_length = 255)
    gambar = models.ImageField(max_length = 255, default="")
    isi = models.TextField()
    kontributor = models.CharField(max_length = 255)
    tanggal = models.DateField(default = timezone.now)
    comment = models.CharField(max_length = 25, default="0")
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, default = "")