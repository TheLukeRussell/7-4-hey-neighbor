from django.views import generic
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


from .models import Tool

User = get_user_model()

def is_super_user_check(user):
    return user.is_superuser

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

class MyToolView(generic.ListView):
    template_name = 'tools/my_tools.html'
    model = Tool
    def get_queryset(self):
        return Tool.objects.filter(owner=self.request.user)

class NeighborView(generic.ListView):
    model = Tool
    template_name = 'tools/neighbors.html'
    context_object_name = 'neighbors_list'

    def get_absolute_url(self):
        return reverse('tools:index')

    def get_queryset(self):
        return User.objects.exclude(username='admin')