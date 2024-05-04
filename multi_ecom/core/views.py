from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import Product
from core.models import Contact
# Create your views here.

def frontpage(request):
    products = Product.objects.all()[0:6]
    
    return render(request, 'core/frontpage.html',{
        'products':products
    })

def about(request):
    return render(request, 'core/about.html')

def contact(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the contact form data to the database
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        # add a success message 
        messages.success(request,  "Your message has been sent!")   
        # Redirect to a same page  after POST
        return redirect('contact')  

     # If it's a GET request, just render the contact page
     return render(request, 'core/contact.html')
