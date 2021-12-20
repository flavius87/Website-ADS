from .models import Article
from pages.models import Page

def get_pages(request):

    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug', 'dropdown_one', 'dropdown_two', 'content', 'image')

    return {
        'pages': pages
    }

def get_articles(request):

    articles = Article.objects.filter(public=True).values_list('title', 'content', 'image', 'page_id')
    return {
        'articles': articles
    }