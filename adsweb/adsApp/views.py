from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'index.html', {
        'title': 'Inicio'
    })

def about(request):

    return render(request, 'about.html', {
        'title': 'Sobre nosotros'
    })

def who(request):

    return render(request, 'about/who.html', {
        'title': '¿Quiénes somos?'
    })

def where(request):

    return render(request, 'about/where.html', {
        'title': '¿Dónde construimos?'
    })

def constructions(request):

    return render(request, 'obras.html', {
        'title': 'Obras'
    })

def inProgress(request):

    return render(request, 'obras/inprogress.html', {
        'title': 'Obras en proceso'
    })

def concluded(request):

    return render(request, 'obras/concluded.html', {
        'title': 'Obras entregadas'
    })

def contact(request):

    return render(request, 'contact.html', {
        'title': 'Contacto'
    })