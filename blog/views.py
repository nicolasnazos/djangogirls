from django.shortcuts import render

from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(title__contains='no').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html', {})
