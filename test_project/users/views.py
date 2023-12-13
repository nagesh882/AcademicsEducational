from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def index(request):
    template = loader.get_template("index.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def blog(request):
    template = loader.get_template("blog.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def contact(request):
    template = loader.get_template("contact.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def about(request):
    template = loader.get_template("about.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))