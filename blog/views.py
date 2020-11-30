from concurrent.futures._base import LOGGER

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from blog.forms import PostForm
from core.models import Post


class HomeListView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = Post

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'home.html', context)


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'posts.html'
    model = Post


def about(request):
    return render(request, 'about.html', {'title':'About'})


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'post_detail.html'
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
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


class PostUpdateView(LoginRequiredMixin, UpdateView):
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


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('index')