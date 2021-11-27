from django.db import models


class Article (models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to='images')
    public = models.BooleanField(verbose_name='Publicado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['created_at']

    def __str__(self):

        if self.public:
            public = "(publicado)"
        else:
            public= "(privado)"

        return f"{self.title} creado el {self.created_at} {public}"

class Contact (models.Model):
    name = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    file = models.FileField(default='null')
    description = models.TextField(max_length=400)
    suscription = models.BooleanField()

    class Meta:
       verbose_name = "Contacto"
       verbose_name_plural = "Contactos"
