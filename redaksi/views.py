from django.shortcuts import render
from .models import Redaksi

# Create your views here.
def redaksi(request):
   posts = Redaksi.objects.all()
   return render(
      request, 
      'redaksi/redaksi.html', 
      {
         'redaksi' : posts, 
      }
   )


