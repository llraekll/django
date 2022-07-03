from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):    
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    my_context={
        "my_text": "Welcome human",
        "human": 9283923,
        "my_list": [272,6823,892137],

    }
    return render(request, 'about.html', my_context)

def social_view(request, *args, **kwargs):
    return render(request, 'social.html', {})

#