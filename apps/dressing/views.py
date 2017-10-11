from django.shortcuts import render, reverse, redirect
from .pages_dictionary import pages
from .models import Article, Annotation
from .forms import AddAnnotation

# Create your views here.
def index(request):
    context = {
        'pages': pages
    }
    return render(request, 'dressing/index.html', context)

def get_or_create_article(request):
    if request.POST:
        url = request.POST['url']
        articles = Article.objects.filter(url=url)
        print len(articles)
        if len(articles) < 1:
            Article.objects.create(url=url)
            article = Article.objects.get(url=url)
            print article
            return redirect(reverse('dressing:show', kwargs={'article_id': article.id}))
        else:
            article = articles[0]
            print article.url
            return redirect(reverse('dressing:show', kwargs={'article_id': article.id}))
    else:
        return redirect(reverse('dressing:welcome'))

def show(request, article_id):
    form = AddAnnotation()
    article = Article.objects.get(id=article_id)
    context = {
        'url': article.url,
        'form': form,
    }
    return render(request, 'dressing/white_wall.html', context)