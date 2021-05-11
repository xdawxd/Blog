from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView, DeleteView
    )


class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        # grab all objects from the post model and filter them -> Less Than or Equal to current time and order them descending by date
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # using reverse_lazy function to make sure the user submits the deletion before redirecting
    success_url = reverse_lazy('blog:post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        # drafts should not have publication_date
        return Post.objects.filter(published_date__isnull=True).order_by('creation_date')


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk=pk)

