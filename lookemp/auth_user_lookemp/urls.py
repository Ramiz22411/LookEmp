from django.urls import path
from . import views

urlpatterns = [
    path('register_user', views.RegisterUserView.as_view(), name='create_user'),
    path('list_users', views.ListUserView.as_view(), name='list_users'),
    path('signin', views.SignInView.as_view(), name='signin'),
    path('logout', views.LogoutView.as_view(), name='logout'),

]
