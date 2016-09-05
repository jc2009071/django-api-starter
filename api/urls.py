from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter(schema_title='Pastebin API')
router.register(r'devices', views.DeviceViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth$', views.Auth.as_view()),
]
