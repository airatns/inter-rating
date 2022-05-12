from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import GenresViewSet, CategoriesViewSet, TitlesViewSet

router_v1 = DefaultRouter()
router_v1.register(r'genres', GenresViewSet, basename="genres")
router_v1.register(r'categories', CategoriesViewSet, basename="categories")
router_v1.register(r'titles', TitlesViewSet, basename="titles")

app_name = 'api'

urlpatterns = [
    url('v1/', include(router_v1.urls)),
]
