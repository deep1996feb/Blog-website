from django.shortcuts import render
from .views import *
from blog.models import post
from django.contrib import admin
from . models import post

# Create your views here.
def index(request):
    #posts1 = post()
    # posts1.title = 'Django is one of the famous framework.'
    # posts1.desc = 'Django helps us to make a website less in a time. It is work on Model View Template.'
    # posts1.img = 'django.png'

    # posts2 = post()
    # posts2.title = 'Django is one of the famous for website.'
    # posts2.desc = 'Django helps us to make a website less in a time. It is work on Model View Template.It is faster'
    # posts2.img = 'django1.png'

    # posts3 = post()
    # posts3.title = 'Django has so much built in functions.'
    # posts3.desc = 'Django provides so much in built functions which makes easy to create a websites.'
    # posts3.img = 'django2.jpg'
    # posts = [posts1, posts2, posts3]
    
    posts = post.objects.all()
    return render(request,'index.html', {'posts': posts})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def search(request):
    return render(request,'search.html')
