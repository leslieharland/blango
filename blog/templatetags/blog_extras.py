from django.contrib.auth import get_user_model
user_model = get_user_model()
from django.template import Library
from django.utils import html
from django.utils import safestring
from django.utils.html import format_html

register = Library()

@register.filter
def author_details(author, current_user):
    if not type(author) == user_model:
        return ""
      
    if author == current_user:
        return format_html("<strong>me</strong>")
    if author.first_name and author.last_name:
        name =  f"{author.first_name} {author.last_name}"
    else:
        name = author.username
    
    if author.email:
        email = author.email
        prefix = f'<a href="mailto:{email}">'
        suffix = "</a>"
    else:
        prefix = ""
        suffix = ""

    return format_html(f"{prefix}{name}{suffix}")
      
    