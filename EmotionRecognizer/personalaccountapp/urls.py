from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'list', ResultsModelViewSet, basename='list')

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('settings/', change_password, name='user_settings'),
    path('api/', include(router.urls))
]
