from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from accounts.forms import RegisterForm


class RegisterView(CreateView):
    """
    A CBV for register new user.
    """
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your account has been created! You are now able to log in')
        return response
