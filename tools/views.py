from django.views import generic
from django.conf import settings

from .models import Tools

class IndexView(generic.ListView):
    template_name = 'tools/index.html'
    model = Tools