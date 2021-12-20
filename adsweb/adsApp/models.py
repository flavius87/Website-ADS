from django.db import models

class Contact (models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phono = models.IntegerField(default=0)
    email = models.EmailField(max_length=50)
    city = models.TextField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    

    class Meta:
       verbose_name = "Contacto"
       verbose_name_plural = "Contactos"

