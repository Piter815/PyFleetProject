from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.home, name='blog-main'),
    path('about/', views.about, name='blog-about'),
]