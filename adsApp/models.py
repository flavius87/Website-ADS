from django.core import validators
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator, RegexValidator

class Contact (models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)], verbose_name="Nombre")
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(3)], verbose_name="Apellido")
    phone = PhoneNumberField(blank=True, default="", verbose_name="Teléfono")
    email = models.EmailField(max_length=50, verbose_name="Email")
    city = models.TextField(max_length=150, validators=[RegexValidator('^[A-Za-z-ñ ]*$', 'El campo ciudad no puede contener números o caracteres especiales')], verbose_name="Ciudad")
    subject = models.CharField(max_length=100, validators=[RegexValidator('^[A-Za-z-ñ ]*$', 'El asunto no puede contener números o caracteres especiales')], verbose_name="Asunto")
    description = models.TextField(max_length=400, verbose_name="Tu consulta")
    

    class Meta:
       verbose_name = "Contacto"
       verbose_name_plural = "Contactos"

class Slider(models.Model):
    image = models.ImageField(verbose_name="Imagen", upload_to='slider')
    name = models.CharField(max_length=200, verbose_name="Nombre de la imagen")
    order = models.IntegerField(default=0, verbose_name="Orden de la imagen")