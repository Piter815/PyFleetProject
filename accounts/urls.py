from django.urls import path
from accounts.views import SubmittableLoginView

app_name = 'accounts'

urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
]
