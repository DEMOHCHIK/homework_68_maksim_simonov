from django.contrib import admin
from .models import Article, Comment, ArticleLike, CommentLike


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',  'created_at']
    list_display_links = ['id', 'title']
    # list_filter = ['author']
    search_fields = ['title', 'content']
    fields = ['title',  'content', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Comment)

admin.site.register(ArticleLike)

admin.site.register(CommentLike)
