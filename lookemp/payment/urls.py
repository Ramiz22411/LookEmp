from django.urls import path
from . import views


urlpatterns = [
    path('transaction/', views.CreatePaymentTransactionAtomic.as_view(), name='transaction'),
    path('transaction_list/', views.ListTransactionView.as_view(), name='transaction_list'),
    path('transaction_update/<int:pk>/', views.UpdateTransactionView.as_view(), name='transaction_update'),
    path('bonus/', views.CreatePaymentBonusAtomic.as_view(), name='bonus'),
    path('bonus_list/', views.ListBonusPaymentView.as_view(), name='bonus'),
]
