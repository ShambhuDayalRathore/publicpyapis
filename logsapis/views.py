from calendar import c
from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from logsapis.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable":"This is my variable value"
    }
    return render(request, 'index.html', context)

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        contact = Contact (name=name,email=email,phone=phone,desc=password,date=datetime.today())
        contact.save()
        messages.success(request, 'Record Added successfully.')
    return render(request, 'registration.html')

def viewRegistration(request):
    Display_Student = Contact.objects.all()    
    return render(request,'viewRegistration.html',{'Display_Student':Display_Student})
