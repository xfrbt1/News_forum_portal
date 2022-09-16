from django.http import HttpResponse
from django.shortcuts import render, redirect


def news(request):
    return render(request, 'news/news_page.html')
