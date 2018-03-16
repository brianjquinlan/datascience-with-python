from django.contrib import admin
from .models import Command, Library, DataFrame, PythonLibrary, Algorithm


class CommandAdmin(admin.ModelAdmin):
    list_display = ('library', 'section', 'title')
    list_filter = ('section',)

    order_by = 'library'

admin.site.register(Command, CommandAdmin)
admin.site.register(Library)
admin.site.register(DataFrame)
admin.site.register(PythonLibrary)
admin.site.register(Algorithm)
