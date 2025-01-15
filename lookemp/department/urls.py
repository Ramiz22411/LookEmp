from django.urls import path
from . import views

urlpatterns = [
    path('', views.DepartmentCreateView.as_view(), name='create_department'),
    path('list/', views.DepartmentListView.as_view(), name='list_department'),
    # path('<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),

]
