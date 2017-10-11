from django.shortcuts import render, reverse, redirect
from .pages_dictionary import pages
from .models import Article, Annotation
from .forms import AddAnnotation, Comment

import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

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
    AnnotationForm = AddAnnotation()
    ResponseForm = Comment()
    article = Article.objects.get(id=article_id)
    context = {
        'article_id': article_id,
        'url': article.url,
        'AnnotationForm': AnnotationForm,
        'ResponseForm': ResponseForm,
    }
    return render(request, 'dressing/white_wall.html', context)

def add_annotation(request, article_id):
    user = request.user
    logging.info(user)
    logging.info(article_id)

    form = AddAnnotation(request.POST)
    if form.is_valid():
        form = form.cleaned_data
        new_annotation = Annotation.objects.create(
            subject=form['subject'], 
            body=form['body'], 
            category=form['category'],
            user = user,
            article = article_id,
        )
    return redirect(reverse('dressing:show', kwargs={'article_id': article_id}))