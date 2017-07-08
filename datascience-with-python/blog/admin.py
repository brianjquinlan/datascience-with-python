from django.contrib import admin

from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'published', )
    search_fields = ('title',)
    date_hierarchy = 'published'
    exclude = ('slug', 'views',)

# admin.site.register(Post)
