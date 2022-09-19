from django.contrib import admin
from forum.models import Comment, Post, Category


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

