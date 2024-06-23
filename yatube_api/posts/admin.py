from django.contrib import admin

from .models import Group, Post, Comment, Follow


class GroupAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_editable = ('description',)
    list_display = ('pk', 'title', 'slug', 'description',)
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_editable = ('group',)
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    list_filter = ('pub_date',)
    search_fields = ('text',)


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Follow)
