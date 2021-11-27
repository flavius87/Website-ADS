from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('sobre-nosotros/', views.about, name="sobre_nosotros"),
    #path('sobre-nosotros/quienes-somos', views.who, name="quienes_somos"),
    path('sobre-nosotros/donde-construimos', views.where, name="donde_construimos"),
    path('obras/', views.constructions, name="obras"),
    path('obras/en-proceso', views.inProgress, name="en_proceso"),
    path('obras/entregadas', views.concluded, name="entregadas"),
    path('services/', views.services, name="servicios"),
    path('contacto/', views.contact, name="contacto"),
]

