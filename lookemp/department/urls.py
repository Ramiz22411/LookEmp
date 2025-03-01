from django.urls import path
from . import views

urlpatterns = [
    path('create', views.DepartmentCreateView.as_view(), name='create_department'),
    path('list', views.DepartmentListView.as_view(), name='list_department'),
    path('edit/<int:pk>', views.EditDepartmentView.as_view(), name='edit_department'),
    path('delete/<int:pk>', views.DeleteDepartmentView.as_view(), name='delete_department'),
    path('<int:pk>', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('staff_create', views.StaffCreateView.as_view(), name='create_staff'),
    path('staff_list', views.StaffListView.as_view(), name='list_staff'),
    # path('<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),

]
