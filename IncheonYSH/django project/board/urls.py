from django.urls import path
from django.urls import include
from board import views
from .views import article
from .views import write

app_name = 'board'

urlpatterns = [
    path('article/<int:article_num>', views.article, name='article'),
    path('write', views.write, name='write'),
    path('modify/<int:article_num>', views.modify, name='modify'),
    path('delete/<int:article_num>', views.delete, name='delete'),
    path('write_comment/<int:article_num>', views.write_comment, name='write_comment'),
    path('delete_comment/<int:comment_num>', views.delete_comment, name='delete_comment'),
    path('', views.index, name='index'),
]