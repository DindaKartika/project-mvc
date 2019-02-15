from django.shortcuts import render,redirect
from .models import Contact
from .form import Contact_form

def contact(request):
   return render(request, 'contact/contact.html', {})

def input_contact(request):
    if(request.method == 'POST'):
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')

    else:
        form = Contact_form()
    return render(request, 'contact/input_contact.html', {'form':form})
        