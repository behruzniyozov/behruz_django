from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner',  'created_at', 'updated_at')
    list_filter = ('owner', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    readonly_fields = ['views_count']