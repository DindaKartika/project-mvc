from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Berita, Ekonomi, OlahRaga, Otomotif
from .forms import NewsForm, EconomyForm, SportForm, OutomotiveForm

# Create your views here.
def home(request):
   berita = Berita.objects.all().order_by('-tanggal')
   ekonomi = Ekonomi.objects.all().order_by('-tanggal')
   olahraga = OlahRaga.objects.all().order_by('-tanggal')
   otomotif = Otomotif.objects.all().order_by('-tanggal')
   return render(request, 'berita/home.html', {'beritas':berita, 'ekonomis':ekonomi, 'olahragas':olahraga, 'otomotifs':otomotif})

def index(request):
   return render(request, 'berita/index.html', {})

def foto(request):
   return render(request, 'berita/foto.html', {})

def hlm_berita(request,id):
   berita = Berita.objects.get(pk=id)
   return render(request, 'berita/berita.html', {'berita':berita})

def hlm_ekonomi(request,id):
   ekonomi = Ekonomi.objects.get(pk=id)
   return render(request, 'berita/ekonomi.html', {'ekonomi':ekonomi})

def hlm_olahraga(request,id):
   olahraga = OlahRaga.objects.get(pk=id)
   return render(request, 'berita/olahraga.html', {'olahraga':olahraga})

def hlm_otomotif(request,id):
   otomotif = Otomotif.objects.get(pk=id)
   return render(request, 'berita/otomotif.html', {'otomotif':otomotif})

def form_berita(request):
   def input(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = NewsForm()
    return render(request, 'berita/form-berita.html', {'form':form})

def form_ekonomi(request):
   def input(request):
    if request.method == "POST":
        form = EconomyForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = EconomyForm()
    return render(request, 'berita/form-ekonomi.html', {'form':form})

def form_otomotif(request):
   def input(request):
    if request.method == "POST":
        form = OutomotiveForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = OutomotiveForm()
    return render(request, 'berita/form-otomotif.html', {'form':form})

def form_olahraga(request):
   def input(request):
    if request.method == "POST":
        form = SportForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = SportForm()
    return render(request, 'berita/form-olahraga.html', {'form':form})