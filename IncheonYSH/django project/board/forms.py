from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Article
from .models import Comment

class WriteArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=30, widget=forms.TextInput)
    maintext = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ['title', 'maintext',]

    """
    def __init__(self, *args, **kwargs):
        super(WriteArticleForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': '필수 입력 필드입니다'}
    """