from django import forms
from .models import Contact
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class ContactForm(forms.ModelForm):

    

    class Meta:
        model = Contact
        fields = ['name', 'last_name', 'phone', 'email', 'city', 'subject', 'description']
        widgets = {
            'name': forms.TextInput(
                        attrs= {
                            'class':"form-control", 
                            'id':"inputName", 
                            'placeholder':"Escribe solo tu nombre",                          
                        }
            ),
            'last_name': forms.TextInput(
                        attrs= {
                            'class':"form-control", 
                            'id':"inputLastName",
                            'placeholder':"Escribe tu apellido",
                        }
            ), 
            'phone': PhoneNumberPrefixWidget(
                        attrs= {
                            'initial':"AR",
                            'class':"form-control", 
                            'id':"inputPhone",
                            'placeholder':"Ingresa tu número de teléfono",
                        }
            ),
            'email': forms.EmailInput(
                        attrs= {
                            'class':"form-control", 
                            'id':"inputEmail",
                            'placeholder':"tuemail@email.com",
                        }
            ),
            'city': forms.TextInput(
                        attrs= {
                            'class':"form-control", 
                            'id':"inputCity",
                            'placeholder':"Ingresa tu ciudad",
                        }
            ),
            'subject': forms.TextInput(
                        attrs= {
                            'class':"form-control", 
                            'id':"contactFormControlInput",
                            'placeholder':"Motivo de la consulta",
                        }
            ),
            'description': forms.Textarea(
                        attrs= {
                            'class':"form-control", 
                            'id':"contactFormDescription",
                            'placeholder':"Escribe tu consulta",
                            'rows':"8"
                        }
            ),
        }



