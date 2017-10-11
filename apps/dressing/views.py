from django.shortcuts import render, reverse, redirect
from .pages_dictionary import pages

from .models import Article, Annotation, Comment
from .forms import AddAnnotation, AddComment
from django.contrib.auth.decorators import login_required

import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
from .services import get_stacked

# Create your views here.
@login_required
def index(request):
    context = {
        'pages': pages
    }
    return render(request, 'dressing/index.html', context)

@login_required
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

@login_required
def show(request, article_id):
    AnnotationForm = AddAnnotation()
    CommentForm = AddComment()
    article = Article.objects.get(id=article_id)
    annotations = article.annotations.all()
    comments = []
    for annotation in annotations:
        comments.append(annotation.comments.all())

    context = {
        'article_id': article_id,
        'url': article.url,
        'annotations': annotations,
        'comments': comments,
        'AnnotationForm': AnnotationForm,
        'CommentForm': CommentForm,
    }
    return render(request, 'dressing/white_wall.html', context)

@login_required
def add_annotation(request, article_id):
    user = request.user
    article = Article.objects.get(id=article_id)

    form = AddAnnotation(request.POST)
    if form.is_valid():
        form = form.cleaned_data
        new_annotation = Annotation.objects.create(
            subject=form['subject'], 
            body=form['body'], 
            category=form['category'],
            user = user,
            article = article,
        )
    return redirect(reverse('dressing:show', kwargs={'article_id': article_id}))

@login_required
def add_comment(request, article_id, annotation_id):
    user = request.user
    annotation = Annotation.objects.get(id=annotation_id)

    logging.info(user)
    logging.info(annotation_id)
    logging.info(annotation)

    form = AddComment(request.POST)
    if form.is_valid():
        form = form.cleaned_data
        comment = Comment.objects.create(
            body=form['body'], 
            user = user,
            annotation = annotation,
        )
    return redirect(reverse('dressing:show', kwargs={'article_id': article_id}))