from django.urls import path
from . import views

urlpatterns = [
    path('', views.other, name='index'),
]