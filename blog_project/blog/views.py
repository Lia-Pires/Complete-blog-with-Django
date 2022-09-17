from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Lia Pires',
        'title': 'Blog Post 1',
        'content': 'This is my first blog post',
        'date_posted': '16th September, 2022',
    },

    {
        'author': 'Pia Lires',
        'title': 'Blog Post 2',
        'content': 'This is my blog post',
        'date_posted': '17th September, 2022',
    }


]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
