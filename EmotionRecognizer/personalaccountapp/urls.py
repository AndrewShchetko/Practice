from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('settings/', change_password, name='user_settings'),
]
