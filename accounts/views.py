from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from accounts.forms import SubmittableAuthenticationForm, SubmittablePasswordChangeForm, SignUpForm


class SubmittableLoginView(LoginView):
    form_class = SubmittableAuthenticationForm
    template_name = 'forms.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    form_class = SubmittablePasswordChangeForm
    template_name = 'forms.html'
    success_url = reverse_lazy('index')


class SuccessMessagedLogoutView(LogoutView):
    def get_next_page(self):
        result = super().get_next_page()
        messages.success(self.request, 'Logout successful')
        return result


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'forms.html'
    success_url = reverse_lazy('index')
