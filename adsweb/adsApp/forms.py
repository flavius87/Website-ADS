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
        
 # this function will be used for the validation
    def clean(self):
 
        # data from the form is fetched using super function
        super(ContactForm, self).clean()
         
        # extract the name and lastname field from the data
        name = self.cleaned_data.get('name')
        last_name = self.cleaned_data.get('last_name')
 
        # conditions to be met for the username length
        if len(name) < 3:
            self._errors['name'] = self.error_class([
                'El nombre no puede tener menos de tres caracteres'])
        
        if len(last_name) <3:
            self._errors['last_name'] = self.error_class([
                'El apellido no puede tener menos de tres caracteres'])
 
        # return any errors if found
        return self.cleaned_data
    