from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .forms import ContactForm
from adsApp.models import Slider

# Create your views here.

def index(request):

    slider = Slider.objects.all().order_by('order')
    context  = {
        'slider' : slider
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        details = ContactForm(request.POST)
        
        if details.is_valid():
            details.save(commit = False)
            return HttpResponse("Formulario enviado correctamente")
        else:
            return render(request, 'contact.html', {'form':details})
   
    else:
        form = ContactForm(None)
        return render(request, 'contact.html', {'form':form})
