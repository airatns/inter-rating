from rest_framework.routers import DefaultRouter
from django.urls import include, path
from users.views import SignUp, Token, UserAccountDetail


router_v1 = DefaultRouter()


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', SignUp.as_view(), name='signup'),
    path('v1/auth/token/', Token.as_view(), name='get_token'),
    path('v1/users/me/', UserAccountDetail.as_view(), name='account_detail')
]


# На users Должны быть символы, написать регулярными выражениями
