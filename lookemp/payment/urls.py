from django.urls import path
from . import views

urlpatterns = [
    path('transaction/', views.CreatePaymentTransactionAtomic.as_view(), name='transaction'),
    path('bonus/', views.CreatePaymentBonusAtomic.as_view(), name='bonus'),
]
