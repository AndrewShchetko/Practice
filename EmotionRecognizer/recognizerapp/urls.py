from django.urls import path, include
from .views import UseNNAPIView, use_nn


urlpatterns = [
    path('home/', use_nn, name="home"),
    path('api/result/', UseNNAPIView.as_view(), name="result-create"),
]
