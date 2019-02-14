from django.shortcuts import render

# Create your views here.
def redaksi(request):
   return render(request, 'redaksi/redaksi.html', {})