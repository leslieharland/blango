from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
import logging

# Create your views here.
def index(request):
    logger = logging.getLogger(__name__)
    posts = Post.objects.filter(published_at__lte=timezone.now())
    logger.debug(timezone.now())
    return render(request, "blog/index.html", {"posts": posts})
