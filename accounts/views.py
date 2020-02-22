from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import generic
from django.contrib.auth import logout
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("tools:index")

def login_request(request):
    form = AuthenticationForm()
    def get_success_url(self):
        return reverse_lazy('tools:index')

