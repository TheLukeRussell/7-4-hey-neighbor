from django.views import generic
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy


from .models import Tool

User = get_user_model()

def is_super_user_check(user):
    return user.is_superuser

class IndexView(generic.ListView):
    template_name = 'tools/index.html'
    model = Tool

class CreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'tools/create.html'
    model = Tool
    fields = ['tool', 'type', 'available']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    def handle_no_permission(self):
        return redirect('login')

class DetailView(generic.DetailView):
    template_name = 'tools/detail.html'
    model = Tool

class EditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'tools/edit.html'
    model = Tool
    fields = ['tool', 'type', 'available']

class BorrowView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'tools/borrow.html'
    model = Tool
    fields = ['available']
    success_url = reverse_lazy('tools/index.html')
    def get_success_url(self):
        return reverse_lazy('tools:index')

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'tools/delete.html'
    model = Tool
    success_url = reverse_lazy('tools/index.html')
    def get_success_url(self):
        return reverse_lazy('tools:index')

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