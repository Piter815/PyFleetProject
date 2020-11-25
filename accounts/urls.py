from django.contrib.auth.views import LoginView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]
