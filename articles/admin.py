from django.contrib import admin

from .models import Article, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    # Controls how many extra empty comment fields appear
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)