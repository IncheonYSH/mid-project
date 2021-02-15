from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    article_number = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='username')
    title = models.CharField(max_length=30)
    maintext = models.TextField()
    time = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return str(self.article_number)


class Comment(models.Model):
    comment_number = models.AutoField(primary_key=True)
    article_number = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='article_number')
    commentcomment_number = models.IntegerField(blank=True, null=True)
    username = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='username')
    comment = models.CharField(max_length=500)
    time = models.DateTimeField()
    def __str__(self):
        return str(self.comment_number)
