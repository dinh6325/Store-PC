# accounts/urls.py
from django.urls import path
from .views import CustomLoginView, register, user_logout

urlpatterns = [
    path('login/',    CustomLoginView.as_view(), name='login'),
    path('logout/',   user_logout,                name='logout'),
    path('register/', register,                   name='register'),
]
