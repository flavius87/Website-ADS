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

    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('inicio')
        else:
            return render(request, 'invalid-form.html', {
        'title': 'Formulario invalido'
    })
   
    return render(request, 'contact.html', {'form':form})
