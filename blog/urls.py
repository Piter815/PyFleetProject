from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [

    path('about/', views.about, name='blog-about'),
]