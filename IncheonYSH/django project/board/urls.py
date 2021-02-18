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
    path('', views.index, name='index')
]