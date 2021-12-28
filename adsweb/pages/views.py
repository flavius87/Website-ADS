from django.shortcuts import render

from .models import Article
from .models import Page

# Create your views here.

def page(request, slug):

    page = Page.objects.get(slug=slug)

    return render(request, "pages/page.html", {
        "title": "Página",
        "page": page
    })

def article(request):

   # Sacar artículos
    article = Article.objects.get().all()

    return render(request,
    {'article':article})

