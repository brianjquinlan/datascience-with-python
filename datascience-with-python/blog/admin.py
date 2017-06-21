from django.contrib import admin

from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published')
    search_fields = ('title')
    raw_id_fields = ('author',)
    date_hierarchy = 'published'

admin.site.register(Post)
