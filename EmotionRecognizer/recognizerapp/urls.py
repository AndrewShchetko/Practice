from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResultsCreateView, use_nn


router = DefaultRouter()
router.register(r'results', ResultsCreateView)

urlpatterns = [
    path('home/', use_nn, name="home"),
    path('api/', include(router.urls))
]
