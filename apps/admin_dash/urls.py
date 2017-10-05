from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='root'),
    url(r'^admin', views.admin_dash, name='admin'),
    url(r'^update/(?P<num>[0-9]+)', views.update, name='update'),
    url(r'^show/(?P<num>[0-9]+)', views.show, name='show'),
    url(r'^edit/(?P<num>[0-9]+)', views.edit, name='edit'),
    url(r'^delete/(?P<num>[0-9]+)', views.delete, name='delete'),
    url(r'^delete_check/(?P<num>[0-9]+)', views.delete_check, name='delete_check'),
]