"""clocktime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from timo import views as timo_views
urlpatterns = [
    url(r'^&admin[c]', include(admin.site.urls)),
    url(r'[H]', timo_views.EmailHome, name='Email.html'),
    url(r'[R]', timo_views.Drivers_Register, name='Dato.html'),
    url(r'[x]', timo_views.Tod, name='x'),
    url(r'[S]', timo_views.Email_SignIn, name='SignUp.html'),
    url(r'[Q]', timo_views.Trip, name='Out.html'),
    url(r'[W]', timo_views.Complete, name='Complete'),
    url(r'[o]', timo_views.logout_view, name='Logout'),
    url(r'[v]', timo_views.sessinvar, name='sessinvar'),
]
