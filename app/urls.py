from django.urls import path
from .views.userviews import UserRegisterView,CurrentUserView




urlpatterns = [
    path('user-profile/', CurrentUserView.as_view(), name='user-profile'),
    path('register/', UserRegisterView.as_view(), name='register'),
   ]