from django.urls import path, include
from .views import ResultsCreateView, use_nn


urlpatterns = [
    path('home/', use_nn, name="home"),
    path('api/result/', ResultsCreateView.as_view(), name="result-create"),
]
