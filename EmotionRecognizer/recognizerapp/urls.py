from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResultsCreateView, ResultsModelViewSet, use_nn


router = DefaultRouter()
router.register(r'list', ResultsModelViewSet, basename='list')

urlpatterns = [
    path('home/', use_nn, name="home"),
    path('api/result/', ResultsCreateView.as_view(), name="result-create"),
    path('api/', include(router.urls))
]
