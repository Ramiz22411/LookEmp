from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from .models import Department


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
