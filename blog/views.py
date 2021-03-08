from django.shortcuts import render

from .models import Post
from django.shortcuts import get_object_or_404


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(title__contains='no').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
