from django.views import generic
from django.conf import settings

from .models import Tool

class IndexView(generic.ListView):
    template_name = 'tools/index.html'
    model = Tool

class CreateView(generic.CreateView):
    template_name = 'tools/create.html'
    model = Tool
    fields = '__all__'

class DetailView(generic.DetailView):
    template_name = 'tools/detail.html'
    model = Tool