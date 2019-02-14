from django.shortcuts import render

# Create your views here.
def home(request):
   return render(request, 'berita/home.html', {})

def index(request):
   return render(request, 'berita/index.html', {})

def foto(request):
   return render(request, 'berita/foto.html', {})

def base(request):
   return render(request, 'base/base.html', {})