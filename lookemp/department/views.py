from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from .models import Department, Staff


# Create your views here.

class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'departments/create_department.html'
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/department_ls.html'


class StaffCreateView(CreateView):
    model = Staff
    template_name = 'departments/create_staff.html'
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class StaffListView(ListView):
    model = Staff
    template_name = 'departments/staff_list.html'
