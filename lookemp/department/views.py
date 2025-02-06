from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import StaffForm
from .models import Department, Staff


# Create your views here.

class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    template_name = 'departments/create_department.html'
    fields = [
        'name_of_department',
        'start_work_time',
        'allowed_lateness',
        'end_work_time',
        'lateness_penalty',
        'lateness_penalty_per_min',
        'sum_penalty',
        'close_attendance',
        'lunch_time',
        'allowed_lunch_time',
        'end_lunch',
        'salary_for_lunch',
        'weekend_days'
    ]
    success_url = '/department/list'

    def form_valid(self, form):
        user = self.request.user
        if hasattr(user, 'company'):  # Проверяем, есть ли у пользователя связанная компания
            form.instance.company = user.company
            return super().form_valid(form)
        else:
            messages.error(self.request, "Ошибка: У вашего пользователя нет привязанной компании.")
            return redirect('/')  # Укажите страницу ошибки


class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/department_ls.html'
    context_object_name = 'departments'


class StaffCreateView(CreateView):
    model = Staff
    template_name = 'departments/create_staff.html'
    form_class = StaffForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class StaffListView(ListView):
    model = Staff
    template_name = 'departments/staff_list.html'
    context_object_name = 'staffs'
