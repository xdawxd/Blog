from blog.models import Post, Comment
from blog.forms import CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


# rewrite to CreateView
class CommentView(View):
    form_class = CommentForm
    model = Comment
    template_name = 'blog/comment_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(request, self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        post = get_object_or_404(Post, pk=kwargs['pk'])

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('blog:post_detail', pk=kwargs['pk'])


class CommentApprove(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        comment.approve()
        return redirect('blog:post_detail', pk=comment.post.pk)


class CommentRemove(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        comment =  get_object_or_404(Comment, pk=kwargs['pk'])
        post_pk = comment.post.pk
        comment.delete()
        return redirect('blog:post_detail', pk=post_pk)
