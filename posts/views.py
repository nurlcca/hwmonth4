from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'posts/post_list.html', {'posts': posts})