from pages.models import Page, Asside, Gallery, GalleryImages, Video, Article

def get_pages(request):

    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug', 'dropdown_one', 'dropdown_two', 'content', 'image')

    return {
        'pages': pages
    }

def get_assides(request):

    assides = Asside.objects.values_list('id', 'header', 'title', 'content')
    return {
        'assides': assides
    }

def get_galleries(request):

    galleries = Gallery.objects.values_list('id', 'title', 'description', 'image')
    return {
        'galleries': galleries
    }

def get_galleriesImg(request):

    galleriesImg = GalleryImages.objects.values_list('id', 'image')
    return {
        'galleriesImg': galleriesImg
    }

def get_videos(request):

    videos = Video.objects.values_list('caption', 'video')
    return {
        'videos': videos
    }
def get_articles(request):

    articles = Article.objects.values_list('id', 'title', 'content', 'image')
    return {
        'articles': articles
    }