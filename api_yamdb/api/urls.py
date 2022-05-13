from rest_framework.routers import DefaultRouter
from django.urls import include, path
from users.views import SignUpView, TokenView


router_v1 = DefaultRouter()
# router_v1.register('auth/signup/', UserRegistrationView.as_view())


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
    path('v1/auth/token/', TokenView.as_view(), name='get_token'),
]


# На users Должны быть символы, написать регулярными выражениями
