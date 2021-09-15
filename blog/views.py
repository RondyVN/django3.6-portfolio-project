from django.shortcuts import render, get_object_or_404
from .models import News

def all_blogs(requests):
    news = News.objects.order_by('-data')[:5]
    return render(requests, 'blog/all_blogs.html', {'news': news})

def detail(request, blog_id):
    new = get_object_or_404(News, pk=blog_id)
    return render(request, 'blog/detail.html', {'new':new})