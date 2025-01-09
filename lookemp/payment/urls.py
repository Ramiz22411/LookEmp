from django.urls import path
from . import views

urlpatterns = [
    path('transaction/', views.transaction, name='transaction'),
    path('bonus/', views.bonus, name='bonus'),
]