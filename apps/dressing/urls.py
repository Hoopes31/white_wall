from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='welcome'),
    url(r'^show/(?P<article_id>\d+)', views.show, name='show'),
    url(r'^annotate/(?P<article_id>\d+)', views.add_annotation, name='add_annotation'),
    url(r'^get_or_create', views.get_or_create_article, name='get_or_create_article'),
 ]