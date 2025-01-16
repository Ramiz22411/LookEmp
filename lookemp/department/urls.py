from django.urls import path
from . import views

urlpatterns = [
    path('create', views.DepartmentCreateView.as_view(), name='create_department'),
    path('list', views.DepartmentListView.as_view(), name='list_department'),
    path('staff_create', views.StaffCreateView.as_view(), name='create_staff'),
    path('staff_list', views.StaffListView.as_view(), name='list_staff'),
    # path('<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),

]
