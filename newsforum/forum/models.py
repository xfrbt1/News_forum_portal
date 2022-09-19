from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "CATEGORY"
        verbose_name_plural = "CATEGORIES"


class Post(models.Model):
    category = models.ForeignKey(Category, max_length=255, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1500)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    publish_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "POST"
        verbose_name_plural = "POSTS"



class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(max_length=1500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.author}"

    class Meta:
        verbose_name = "COMMENT"
        verbose_name_plural = "COMMENTS"


