from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.index, name='welcome'),
    url(r'^show/(?P<num>[0-9]+)', views.choose_article, name='choose_article'), 
]