from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment
from blog.forms import CommentForm

# rewrite to classes later on...
@login_required
def comment_add(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', pk=post.pk)

    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', context={'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment =  get_object_or_404(Comment, pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
