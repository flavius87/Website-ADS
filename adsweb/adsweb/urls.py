"""adsweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('sobre-nosotros/', views.about, name="sobre nosotros"),
    path('sobre-nosotros/quienes-somos', views.who, name="quiénes somos"),
    path('sobre-nosotros/donde-construimos', views.where, name="dónde construimos"),
    path('obras/', views.constructions, name="obras"),
    path('obras/en-proceso', views.inProgress, name="en proceso"),
    path('obras/entregadas', views.concluded, name="entregadas"),
    path('contacto/', views.contact, name="contacto"),
]

