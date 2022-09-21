from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView
from forum.forms import PostCreateForm, CommentForm
from forum.models import Post, Comment







@login_required(login_url=reverse_lazy('auth_page'))
def post_detail(request):
    comment_form = CommentForm()
    post = get_object_or_404(Post.pk)
    comments = post.comments.filter()
    if request.method == 'POST':
        author = request.user.username
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            Comment.objects.create(**comment_form.cleaned_data, author=author)
            return redirect('forum')
        else:
            comment_form = CommentForm()
    return render(request, 'forum:post', context={'comment_form': comment_form,
            "comments": comments},)










@login_required(login_url=reverse_lazy('auth_page'))
def forum(request):
    posts = Post.objects.order_by('-publish_time')
    return render(request, 'forum/forum_page.html', {'posts': posts})




@login_required(login_url=reverse_lazy('auth_page'))
def post_create(request):
    if request.method == 'POST':
        author = request.user.username
        form = PostCreateForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data, author=author)
            return redirect('forum')
    else:
        form = PostCreateForm()
    return render(request, 'forum/post_create.html', {'form': form})


