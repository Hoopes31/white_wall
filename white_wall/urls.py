from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from rest import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('apps.user.urls', namespace='login')),
    url(r'^dash/', include('apps.admin_dash.urls', namespace='dash')),
]