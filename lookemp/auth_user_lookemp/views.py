from django.views.generic import ListView, CreateView
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.

class ListUserView(ListView):
    model = User
    template_name = 'auth_user_lookemp/user_ls.html'
    context_object_name = 'users'


class RegisterUserView(CreateView):
    model = User
    fields = ['username', 'email', 'password']
    success_url = '/auth_lookemp/list_users'
    template_name = 'auth_user_lookemp/create_user.html'
