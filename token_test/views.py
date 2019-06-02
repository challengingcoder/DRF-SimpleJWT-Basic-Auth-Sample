from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserView(APIView):
    def get(self, request, format=None):
        if request.user.is_anonymous:
            return JsonResponse({'login_status': False, 'uesr': 'Anonymous User'})

        return JsonResponse({'login_status': True, 'user': request.user.name})

class AuthUserView(APIView):
    authentication_classes = (BasicAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        return JsonResponse({'uesr': request.user.name})

class TokenBaedAuthUserView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        return JsonResponse({'uesr': request.user.name})