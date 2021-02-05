from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title': '특수문자,공백 입력 불가',
    }))
    last_name = forms.CharField(label='last_name')
    email = forms.EmailField(label='email')
    year = forms.CharField(label='year')
    month = forms.CharField(label='month')
    day = forms.CharField(label='day')
    sex = forms.CharField(label='sex')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('last_name', 'email', 'year', 'month', 'day', 'sex',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = get_user_model()
        if user.objects.filter(email=email).exists():
            raise forms.ValidationError('사용중인 이메일입니다')
        return email


