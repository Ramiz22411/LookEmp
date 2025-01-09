from django.urls import path
from . import views

urlpatterns = [
    path('signup_lookemp', views.signup_l, name='auth_lookemp'),
    path('signin_lookemp', views.signin_l, name='auth_lookemp'),
    path('logout_lookemp', views.logout_l, name='auth_lookemp'),
]
