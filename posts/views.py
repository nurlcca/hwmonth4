from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, is_published=True)
    return render(request, 'posts/post_detail.html', {'post': post})