from django.urls import path

from . import views

urlpatterns = [
    path('', views.get), #localhost:8000/api
]