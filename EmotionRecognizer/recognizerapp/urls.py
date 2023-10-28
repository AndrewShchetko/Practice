from django.urls import path
from .views import *


urlpatterns = [
    path('home/', use_nn, name="home"),
]
