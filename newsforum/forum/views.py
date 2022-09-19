from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from forum.forms import PostForm
from forum.models import Post

from forum.models import Post

class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'forum/post_create.html'

    def get_success_url(self):
        return reverse('forum:post', kwargs = {'pk': self.object.id})


class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post_detail.html'



def forum(request):
    posts = Post.objects.order_by('-publish_time')
    return render(request, 'forum/forum_page.html', {'posts': posts})




