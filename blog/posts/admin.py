from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','post_title']
    list_display_links = ['post_title']
    list_filter = ['post_title']
    search_fields = ['post_title']
# admin.site.register(Post,PostAdmin)
