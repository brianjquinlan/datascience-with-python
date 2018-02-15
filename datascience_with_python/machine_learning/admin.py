from django.contrib import admin
from .models import Command, DataFrames


class CommandAdmin(admin.ModelAdmin):
    list_display = ('library', 'section', 'title')
    list_filter = ('section',)

    order_by = 'library'


admin.site.register(Command, CommandAdmin)
admin.site.register(DataFrames)

