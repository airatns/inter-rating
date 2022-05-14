from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from rest_framework_nested import routers
from users.views import SignUp, Token, UserAccountDetail

from .views import GenresViewSet, CategoriesViewSet, TitlesViewSet, ReviewViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('genres', GenresViewSet, basename="genres")
router_v1.register('categories', CategoriesViewSet, basename="categories")
router_v1.register('titles', TitlesViewSet, basename="titles")


nested_router_v1 = routers.NestedDefaultRouter(router_v1, 'titles',
                                               lookup='title')
nested_router_v1.register('reviews', ReviewViewSet, basename='reviews')
urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include(nested_router_v1.urls)),
    path('v1/auth/signup/', SignUp.as_view(), name='signup'),
    path('v1/auth/token/', Token.as_view(), name='get_token'),
    path('v1/users/me/', UserAccountDetail.as_view(), name='account_detail')
]

# На users Должны быть символы, написать регулярными выражениями
