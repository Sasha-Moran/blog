from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from .models import Post, Tag


def post_list(request):
    posts = Post.objects.all()[:10]
    return render(request, 'blog/post_list.html', context={'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', context={'post': post})


def posts_with_tag(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_with_tag.html', context={'tag': tag})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
