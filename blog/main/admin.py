from django.contrib import admin
from .models import Article, ContentImage


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('is_published', )


class ContentImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'content_image')
    list_display_links = ('id', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(ContentImage, ContentImageAdmin)
