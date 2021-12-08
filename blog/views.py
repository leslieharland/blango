from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

import logging

# Create your views here.
def index(request):
    logger = logging.getLogger(__name__)
    posts = Post.objects.filter(published_at__lte=timezone.now())
    logger.debug(timezone.now())
    return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})