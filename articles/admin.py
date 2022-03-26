from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline): # new
    model = Comment
    extra=0
class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
    CommentInline,
    ]


# Register your models here.
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)