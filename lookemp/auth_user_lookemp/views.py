from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, View
from django.contrib.auth import authenticate, login, logout
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

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SignInView(View):
    template_name = 'auth_user_lookemp/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/auth_lookemp/list_users')
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
            return render(request, self.template_name)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/auth_lookemp/signin')
