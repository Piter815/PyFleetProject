from accounts.views import SubmittableLoginView, SuccessMessagedLogoutView, SubmittablePasswordChangeView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
]
