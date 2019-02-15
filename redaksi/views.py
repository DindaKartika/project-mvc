from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Redaksi

# Create your views here.
def redaksi(request):
   return render(request, 'redaksi/redaksi.html', {})