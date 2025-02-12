from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CompanyCreateView.as_view(), name='company_create'),
    path('list', views.CompanyListView.as_view(), name='company_list'),
    path('<int:pk>/delete', views.DeleteCompanyView.as_view(), name='company_delete'),
    path('<int:pk>/update', views.UpdateCompanyView.as_view(), name='company_update'),
    path('<int:pk>/detail', views.CompanyDetailView.as_view(), name='company_detail'),
]
