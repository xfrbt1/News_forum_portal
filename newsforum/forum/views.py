from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from forum.forms import PostCreateForm, CommentCreateForm
from forum.models import Post, Comment


class PostsView(View):

    def get(self, request):
        posts = Post.objects.order_by('-publish_time')
        return render(request, "forum/forum_page.html", {'posts': posts})


class PostDetailView(View):

    def get(self, request, pk):
        post = Post.objects.get(id = pk)
        post_comments = Comment.objects.filter(post_id=post)
        comment_form = CommentCreateForm()
        return render(request, 'forum/post_detail.html', {'post':post,'post_comments':post_comments, 'comment_form': comment_form}  )




@login_required(login_url=reverse_lazy('auth_page'))
def post_detail_view(request, pk):
    post = Post.objects.get(id = pk)
    post_comments = Comment.objects.filter(post_id=post)
    if request.method == "POST":
        comment_form = CommentCreateForm(request.POST)
        if comment_form.is_valid():
            Comment.objects.create(**comment_form.cleaned_data, author=request.user.username, post_id=post.pk)
            return redirect('forum')
    else:
        comment_form = CommentCreateForm()
    return render(request, 'forum/post_detail.html', {'post': post, 'post_comments': post_comments, 'comment_form': comment_form})




@login_required(login_url=reverse_lazy('auth_page'))
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data, author=request.user.username)
            return redirect('forum')
    else:
        form = PostCreateForm()
    return render(request, 'forum/post_create.html', {'form': form})



