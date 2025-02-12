from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from company.models import Company


# Create your views here.

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = 'company/company_create.html'
    fields = ('name', 'balance', 'subscription_end')
    success_url = '/company/list'

    def form_valid(self, form):
        return super().form_valid(form)


class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'company/company_ls.html'


class DeleteCompanyView(LoginRequiredMixin, DeleteView):
    model = Company
    success_url = "/company/list"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Company
    context_object_name = 'companies'
    template_name = 'company/update_company.html'
    fields = ('name', 'balance', 'subscription_end')
    success_url = '/company/list'

    def form_valid(self, form):
        return super().form_valid(form)

class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company
    context_object_name = 'company'
    template_name = 'company/company_detail.html'