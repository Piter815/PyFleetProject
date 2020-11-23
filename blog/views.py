from django.shortcuts import render
from django.http import HttpResponse

from core.models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title':'About'})

