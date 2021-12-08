from django.contrib.auth import get_user_model
user_model = get_user_model()
from django.template import Library
from django.utils import html
from django.utils import safestring
from django.utils.html import format_html
from blog.models import Post
from django.db.models import Q
import logging

register = Library()
logger = logging.getLogger(__name__)

@register.filter
def author_details(author, current_user = None):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)
  
# @register.simple_tag(takes_context=True)
# def post_list(context):
#     request = context["request"]
#     current_user = request.user
    
#     #postList = Post.objects.filter(~Q(author=current_user)).latest('published_at')[:5]
#     postList = Post.objects.exclude(author=current_user).latest('published_at')[:5]
#     return {"title": "Recent Posts", "posts": posts}
  
@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    
    #postList = Post.objects.filter(~Q(author=current_user)).latest('published_at')[:5]
#     posts = Post.objects.exclude(pk=post.pk).order_by('published_at')[:5]
#     
#     return {"title": "Recent Posts", "posts": posts}
    posts = Post.objects.exclude(pk=post.pk)[:5]
    logger.debug(posts)
    return {"title": "Recent Posts", "posts": posts}
  
@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def endrow():
    return format_html("</div>")

      
@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)
  
@register.simple_tag
def endcol():
    return format_html("</div>")
  