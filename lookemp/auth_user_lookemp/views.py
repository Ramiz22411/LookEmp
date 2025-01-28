from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView
from django.contrib.auth import get_user_model
from .forms import CustomBaseUserCreationForm

User = get_user_model()


# Create your views here.

class ListUserView(ListView):
    model = User
    template_name = 'auth_user_lookemp/user_ls.html'
    context_object_name = 'users'


class RegisterUserView(SuccessMessageMixin, CreateView):
    form_class = CustomBaseUserCreationForm
    template_name = 'auth_user_lookemp/create_user.html'
    success_url = '/auth_lookemp/list_users'
    success_message = 'Congratulations, you are registered!'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
