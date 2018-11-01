try:
    from django.conf.urls import url, include
except ImportError:
    from django.conf.urls.defaults import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"many_data", views.DataViewSet, basename='data')

router2 = DefaultRouter()
router2.register(r"many_data2", views.DataViewSet, basename='data2')

urlpatterns = [
    url(r"", include(router.urls))
]

app_name = 'api_v1'
