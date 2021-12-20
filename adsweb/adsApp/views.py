from django.shortcuts import redirect, render

from .forms import ContactForm

# Create your views here.

def index(request):

    return render(request, 'index.html', {
        'title': 'Inicio'
    })

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
