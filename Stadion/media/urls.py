from django.urls import path
from . import views

urlpatterns = [
    path('media', views.mediaPage, name='mediaPage'),
]


