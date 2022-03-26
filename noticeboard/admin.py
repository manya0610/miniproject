from django.contrib import admin
from .models import Notice, Comment


class CommentInline(admin.TabularInline): # new
    model = Comment
    extra=0
class NoticeAdmin(admin.ModelAdmin): # new
    inlines = [
    CommentInline,
    ]


# Register your models here.
admin.site.register(Notice,NoticeAdmin)
admin.site.register(Comment)