from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import StaffForm, DepartmentForm
from .models import Department, Staff


# Create your views here.

class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    template_name = 'departments/create_department.html'
    form_class = DepartmentForm
    success_url = '/department/list'

    def form_valid(self, form):
        user = self.request.user
        if hasattr(user, 'company'):  # Проверяем, есть ли у пользователя связанная компания
            form.instance.company = user.company
            return super().form_valid(form)
        else:
            messages.error(self.request, "Ошибка: У вашего пользователя нет привязанной компании.")
            return redirect('/')  # Укажите страницу ошибки


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'departments/department_ls.html'
    context_object_name = 'departments'


class EditDepartmentView(LoginRequiredMixin, UpdateView):
    model = Department
    template_name = 'departments/update_department.html'
    context_object_name = 'departments'
    form_class = DepartmentForm
    success_url = '/department/list'


class DeleteDepartmentView(LoginRequiredMixin, DeleteView):
    model = Department
    success_url = '/department/list'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DepartmentDetailView(LoginRequiredMixin, DetailView):
    model = Department
    template_name = 'departments/department_detail.html'
    context_object_name = 'department'


class StaffCreateView(LoginRequiredMixin, CreateView):
    model = Staff
    template_name = 'departments/create_staff.html'
    form_class = StaffForm
    success_url = '/staff_list'

    def form_valid(self, form):
        user = self.request.user
        if hasattr(user, 'company'):  # Проверяем, есть ли у пользователя связанная компания
            form.instance.company = user.company
            return super().form_valid(form)
        else:
            messages.error(self.request, "Ошибка: У вашего пользователя нет привязанной компании.")
            return redirect('/')  # Укажите страницу ошибки


class StaffListView(LoginRequiredMixin, ListView):
    model = Staff
    template_name = 'departments/staff_list.html'
    context_object_name = 'staffs'
