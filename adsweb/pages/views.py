from django.shortcuts import render

from .models import Article, Asside, Gallery, GalleryImages, Video
from .models import Page

# Create your views here.

def page(request, slug):

    page = Page.objects.get(slug=slug)

    return render(request, "pages/page.html", {
        "title": "Página",
        "page": page
    })

def asside(request):

   # Sacar artículos periodísticos
    asside = Asside.objects.get().order_by("-id")

    return render(request,
    {'asside':asside})

def gallery(request):

   # Galería de fotos
    gallery = Gallery.objects.get().order_by("-id")

    return render(request, 'layout.html',
    {'gallery':gallery})

def galleryImg(request):

   # Galería de fotos
    galleryImg = GalleryImages.objects.get().order_by("-id")

    return render(request, 'layout.html',
    {'galleryImg':galleryImg})

def video(request):

    video = Video.objects.all()

    return render(request, 'layout.html', {'video':video})

def article(request):

   # Sacar artículos
    article = Article.objects.get()

    return render(request,
    {'article':article})