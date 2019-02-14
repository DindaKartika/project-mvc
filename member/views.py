from django.shortcuts import render

# Create your views here.
def signup(request):
   return render(request, 'member/sign-up.html', {})

def login(request):
   return render(request, 'member/login.html', {})

def logout(request):
   return render(request, 'member/logout.html', {})