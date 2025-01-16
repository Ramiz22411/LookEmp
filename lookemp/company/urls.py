from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CompanyCreateView.as_view(), name='company_create'),
    path('list', views.CompanyListView.as_view(), name='company_list'),
]
