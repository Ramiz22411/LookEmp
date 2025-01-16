from django.shortcuts import render
from django.views.generic import ListView, CreateView

from company.models import Company


# Create your views here.

class CompanyCreateView(CreateView):
    model = Company
    template_name = 'company/company_create.html'
    fields = ('name', 'balance', 'subscription_end')
    success_url = '/company/list'

    def form_valid(self, form):
        return super().form_valid(form)


class CompanyListView(ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'company/company_ls.html'
