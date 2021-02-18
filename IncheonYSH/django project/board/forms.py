from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Article
from .models import Comment

class WriteArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': '제목을 입력하세요'}))
    maintext = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ['title', 'maintext',]

class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=500, widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ['comment',]