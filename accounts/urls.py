# file_api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileViewSet
from . import views

router = DefaultRouter()
router.register(r'files', FileViewSet)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('', include(router.urls)),
]




   

