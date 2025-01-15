from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView


class HomeView(TemplateView):
    template_name = 'core/index.html'
