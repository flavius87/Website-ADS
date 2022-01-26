from email.policy import default
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Page(models.Model):
    title = models.CharField(max_length=60, verbose_name="Título")
    content = RichTextUploadingField(verbose_name="Contenido", blank=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='images', blank=True, default=None)
    slug = models.SlugField(unique=True, max_length=150, verbose_name="URL amigable")
    order = models.IntegerField(default=0, verbose_name="Orden de página")
    dropdown_one = models.BooleanField(default=False, verbose_name="Menú desplegable uno")
    dropdown_two = models.BooleanField(default=False, verbose_name="Menú desplegable dos")
    gallery = models.BooleanField(default=False, verbose_name="¿Galería?")
    visible = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.title

class Article (models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    content = RichTextUploadingField(verbose_name='Contenido')
    image = models.ImageField(blank=True, default=None, verbose_name='Imagen', upload_to='images')
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

        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=60, verbose_name="Título")
    description = RichTextUploadingField(default=False, verbose_name="Descripción")
    image = models.ImageField(blank=True, default=None, verbose_name='Imagen', upload_to='images')

    def __str__(self):
        return str(self.title)

class GalleryImages(models.Model):
    gallery = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, default=None, verbose_name='Imagen', upload_to='images')

    def __str__(self):
        return str(self.image)



class Asside(models.Model):
    header = models.CharField(max_length=150, verbose_name='Encabezado')
    title = models.CharField(max_length=150, verbose_name='Título')
    content = RichTextUploadingField(verbose_name='Contenido')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = "Margen"
        verbose_name_plural = "Márgenes"
        ordering = ['created_at']

    def __str__(self):
        return self.title

class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos')

    
    def __str__(self):
        return self.caption
