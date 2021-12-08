from django.contrib import admin


# Register your models here.
from blog.models import Post, Tag, Comment



class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'content_object')
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)