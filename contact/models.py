from django.db import models
from django.utils import timezone

class Contact(models.Model):
    nama = models.CharField(max_length =100)
    email = models.CharField(max_length =255)
    masukan = models.TextField(max_length =1000)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nama
# Create your models here.
