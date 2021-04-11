from django.contrib import admin

from .models import AdvancedUser, Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'published_date']
    list_display_links = ['author', 'title', 'published_date']


class AdvancedUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'date_joined']

admin.site.register(AdvancedUser, AdvancedUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
