from django.contrib import admin
from django.urls import path
from .views import UserView, AuthUserView, AuthUserView, TokenBaedAuthUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),            # get token for simplejwt
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),           # refresh token for simple jwt
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),              # verifying token for simple jwt 


    path('api/get_user/', UserView.as_view(), name='get_user'),                             # 3.a get user 3.a return user name for both 
    path('api/get_auth_user/', AuthUserView.as_view(), name='get_auth_user'),               # 3.b get auth user with simplejwt or basic auth
    path('api/get_token_auth_user/', TokenBaedAuthUserView.as_view(), name='get_token_auth_user'),   # 3.c get auth user only with simplejwt
]
