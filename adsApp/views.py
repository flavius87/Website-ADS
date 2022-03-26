from django.http.response import BadHeaderError
from django.shortcuts import render

from .forms import ContactForm
from adsApp.models import Slider
from django.core.mail import send_mail

# Create your views here.

def index(request):

    slider = Slider.objects.all().order_by('order')
    context  = {
        'slider' : slider
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save(commit = False)
            subject = "Consulta desde el sitio web"
            body = {
			'name': form.cleaned_data['name'], 
			'last_name': form.cleaned_data['last_name'],
            'phone': form.cleaned_data['phone'],
			'email': form.cleaned_data['email'], 
            'city': form.cleaned_data['city'],
            'subject': form.cleaned_data['subject'],
            'description': form.cleaned_data['description'],
            }
           
            message = "\n".join(map(str, body.values()))
    
            try:
                send_mail(subject, message, 'ads.construccionpampeana@gmail.com', ['ads.construccionpampena@gmail.com']) 
            except BadHeaderError:
                return render(request, 'invalid-form.html')
            return render(request, 'valid-form.html')
        else:
            return render(request, 'contact.html', {'form':form})
    else:
        form = ContactForm(None)
        return render(request, 'contact.html', {'form':form})


def work(request):

    return render(request, 'work-us.html')