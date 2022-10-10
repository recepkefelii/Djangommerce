from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("register/", views.SignUpView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path('profile/',views.RetrieveUserView.as_view(),name='check'),
    path('emailverification/',views.VerificationUserView.as_view(),name='emailverification'),
    path('jwt/create/',TokenObtainPairView.as_view(),name='jwt_created'),
    path('jwt/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(),name='token_verify'),
    
]