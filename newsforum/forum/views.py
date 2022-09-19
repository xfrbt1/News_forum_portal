from django.http import HttpResponse
from django.shortcuts import render, redirect


def forum(request):
    return render(request, 'forum/forum_page.html')


