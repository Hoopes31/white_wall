from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.login_page, name='login'),
    url(r'^auth', views.auth, name='auth'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^sign_up', views.sign_up, name='sign_up'),
    url(r'^create', views.create_user, name='create'),
    url(r'^welcome/(?P<name>[a-zA-Z0-9_]*$)', views.welcome, name='welcome'),
]

