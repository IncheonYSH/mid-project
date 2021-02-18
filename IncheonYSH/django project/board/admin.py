from django.contrib import admin
from .models import Article
from .models import Comment
from django.db import models

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
