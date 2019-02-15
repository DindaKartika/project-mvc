from django import forms
from .models import Berita, Ekonomi, OlahRaga, Otomotif

class NewsForm(forms.ModelForm):
    class Meta:
        model = Berita
        fields = ('judul', 'gambar', 'isi', 'kontributor')

class EconomyForm(forms.ModelForm):
    class Meta:
        model = Ekonomi
        fields = ('judul', 'gambar', 'isi', 'kontributor')

class SportForm(forms.ModelForm):
    class Meta:
        model = OlahRaga
        fields = ('judul', 'gambar', 'isi', 'kontributor')

class OutomotiveForm(forms.ModelForm):
    class Meta:
        model = Otomotif
        fields = ('judul', 'gambar', 'isi', 'kontributor')
