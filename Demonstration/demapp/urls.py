from django.urls import path
from .views import *


urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('settings/', change_password, name='user_settings'),
    path('home/', use_nn, name="home"),
]
