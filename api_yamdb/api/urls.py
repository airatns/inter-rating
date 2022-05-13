from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from users.views import SignUpView, TokenView
from .views import GenresViewSet, CategoriesViewSet, TitlesViewSet


app_name = 'api'


router_v1 = DefaultRouter()
router_v1.register(r'genres', GenresViewSet, basename="genres")
router_v1.register(r'categories', CategoriesViewSet, basename="categories")
router_v1.register(r'titles', TitlesViewSet, basename="titles")


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
    path('v1/auth/token/', TokenView.as_view(), name='get_token'),
]




# На users Должны быть символы, написать регулярными выражениями
