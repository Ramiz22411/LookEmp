from django.shortcuts import render


# Create your views here.

def index(request):
    template = 'core/index.html'
    return render(request, template)
