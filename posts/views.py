from django.shortcuts import render, get_object_or_404
from .models import Post, Tag


def post_list(request):
    tag_id = request.GET.get('tag')
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    tags = Tag.objects.all()

    if tag_id:
        posts = posts.filter(tags__id=tag_id)

    return render(request, 'posts/post_list.html', {
        'posts': posts,
        'tags': tags,
        'selected_tag': tag_id,
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, is_published=True)
    return render(request, 'posts/post_detail.html', {'post': post})