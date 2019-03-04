from django.contrib import admin
from testap.models import Post
from testap.models import Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields={'slug':('title',)}
    search_fields=('title','body')
    list_filter=('status','author')
class PostComment(admin.ModelAdmin):
    list_display=['name','email','post','body','created','updated','active']
    list_filter=('active','created','updated')
    search_fields=('name','email','body')

admin.site.register(Post,PostAdmin,)
admin.site.register(Comment,PostComment,)
