from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

# Create your views here.
def home_view(request):
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html")

def about_view(request):
    my_context = {
        'text':'This is about me',
        'mynumber': 123,
        'my_list': [12,13,15, "Abc"],
    } 
    return render(request, "about.html", my_context)

def contact_view(request):
    return render(request, "contact.html")

def social_view(request):
    return HttpResponse("<h1>Social World</h1>")