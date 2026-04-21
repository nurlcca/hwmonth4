from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Tag
from .forms import UserUpdateForm


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


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'posts/edit_profile.html', {'form': form})