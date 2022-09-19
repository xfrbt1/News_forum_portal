from django.http import HttpResponse
from django.shortcuts import render, redirect
from news.models import News


def news(request):
    news = News.objects.order_by('-time')
    return render(request, 'news/news_page.html', {'news': news})
