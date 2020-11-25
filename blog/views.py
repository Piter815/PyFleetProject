from concurrent.futures._base import LOGGER

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from core.models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)

def list(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts.html', context)

def about(request):
    return render(request, 'about.html', {'title':'About'})


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post


class PostCreateView(CreateView):
    title = 'Create Post'
    template_name = 'forms.html'
    form_class = PostForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class PostUpdateView(UpdateView):
    title = 'Edit Post'
    model = Post
    template_name = 'forms.html'
    form_class = PostForm
    success_url = reverse_lazy('index')

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('index')
        return super().form_invalid(form)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('index')