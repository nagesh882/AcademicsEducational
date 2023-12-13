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


def login(request):
    template = loader.get_template("login.html")
    
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


def register(request):
    template = loader.get_template("register.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def python(request):
    template = loader.get_template("python.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

def news_single(request):
    template = loader.get_template("news-single.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def experence(request):
    template = loader.get_template("experence.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def fplace(request):
    template = loader.get_template("fplace.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def eplace(request):
    template = loader.get_template("eplace.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

def tens(request):
    template = loader.get_template("tens.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

def campus(request):
    template = loader.get_template("campus.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def clients(request):
    template = loader.get_template("clients.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))