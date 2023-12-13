from django.urls import path
from . import views 

urlpatterns = [


    path('', views.index, name='index'),
    
    path('blog', views.blog, name='blog'),

    path('contact', views.contact, name='contact'),

    path('about', views.about, name='about'),

    path('login', views.login, name='login'),

    path('register', views.register, name='register'),

    path('python', views.python, name='python'),

    path('news-single', views.news_single, name='news-single'),

    path('experence', views.experence, name='experence'),

    path('fplace', views.fplace, name='fplace'),

    path('eplace', views.eplace, name='eplace'),

    path('tens', views.tens, name='tens'),

    path('campus', views.campus, name='campus'),

]