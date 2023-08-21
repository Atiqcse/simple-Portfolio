
from django.shortcuts import render, HttpResponse
from home.models import contact as ContactModel  # Renaming the model class

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def contact_form(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        
        # Create an instance using the renamed model class
        contact_instance = ContactModel(name=name, email=email, phone=phone, desc=desc)
        contact_instance.save()
        print('Data has been saved to the database')
    
    return render(request, 'contact.html')