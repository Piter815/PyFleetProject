from django.contrib.auth.views import LoginView

from accounts.forms import SubmittableAuthenticationForm


class SubmittableLoginView(LoginView):
    form_class = SubmittableAuthenticationForm
    template_name = 'form.html'
