from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from users.views import SignUp, Token, UserAccountDetail, UserViewSet

from .views import GenresViewSet, CategoriesViewSet, TitlesViewSet, \
    ReviewViewSet, CommentViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('genres', GenresViewSet, basename="genres")
router_v1.register('categories', CategoriesViewSet, basename="categories")
router_v1.register('titles', TitlesViewSet, basename="titles")
router_v1.register('users', UserViewSet, basename='users')

review_router_v1 = routers.NestedDefaultRouter(router_v1, 'titles',
                                               lookup='title')
review_router_v1.register('reviews', ReviewViewSet, basename='reviews')
comment_router_v1 = routers.NestedDefaultRouter(review_router_v1, 'reviews',
                                                lookup='review')
comment_router_v1.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/auth/signup/', SignUp.as_view(), name='signup'),
    path('v1/auth/token/', Token.as_view(), name='get_token'),
    path('v1/users/me/', UserAccountDetail.as_view(), name='account_detail'),
    path('v1/', include(router_v1.urls)),
    path('v1/', include(review_router_v1.urls)),
    path('v1/', include(comment_router_v1.urls)),
]
