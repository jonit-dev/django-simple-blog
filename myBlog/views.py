from django.shortcuts import render
from django.http import HttpResponse

from post.models import Post  # import Post model from post app


def home(request):
    posts = Post.objects.order_by('title')  # use the post model imported above

    return render(request, 'home.html', {'posts': posts})
