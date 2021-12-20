from django import forms
from django.forms.widgets import Textarea
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'last_name', 'phono', 'email', 'city', 'subject', 'description']
        widgets = {
            'name': forms.TextInput(
                        attrs= {
                            'class':"form-control", 
                            'id':"inputName",
                            'placeholder':"nombre",
                            'required':"required",
                        }
            ),
            'last_name': forms.TextInput(
                        attrs= {
                            'class':"form-control", 
                            'id':"inputLastName",
                            'placeholder':"apellido",
                            'required':"required",
                        }
            ),
            'phono': forms.NumberInput(
                        attrs= {
                            'class':"form-control", 
                            'id':"inputPhone",
                            'placeholder':"+54 9",
                        }
            ),
            'email': forms.EmailInput(
                        attrs= {
                            'class':"form-control", 
                            'id':"inputEmail",
                            'placeholder':"tuemail@email.com",
                            'required':"required",
                        }
            ),
            'city': forms.TextInput(
                        attrs= {
                            'class':"form-control", 
                            'id':"inputCity",
                            'placeholder':"Ingresa tu ciudad",
                            'required':"required",
                        }
            ),
            'subject': forms.TextInput(
                        attrs= {
                            'class':"form-control", 
                            'id':"contactFormControlInput",
                            'placeholder':"asunto",
                        }
            ),
            'description': forms.Textarea(
                        attrs= {
                            'class':"form-control", 
                            'id':"contactFormDescription",
                            'placeholder':"Escribe tu consulta",
                            'required':"required",
                        }
            ),
        }
        
        
    
    