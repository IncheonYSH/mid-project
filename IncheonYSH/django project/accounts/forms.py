from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title': '특수문자,공백 입력 불가',
    }))
    last_name = forms.CharField(label='last_name')
    email = forms.EmailField(label='email')
    year = forms.CharField(label='year')
    # month = forms.CharField(label='month')
    day = forms.CharField(label='day')
    # sex = forms.CharField(label='sex')
    month_select = (
        ("01", "1"),
        ("02", "2"),
        ("03", "3"),
        ("04", "4"),
        ("05", "5"),
        ("06", "6"),
        ("07", "7"),
        ("08", "8"),
        ("09", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
    )
    month = forms.ChoiceField(choices=month_select)
    sex_select = (
        ("M", "남자"),
        ("F", "여자"),
    )
    sex = forms.ChoiceField(choices=sex_select)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'last_name', 'email',
            'year',
            'month',
            'day',
            'sex',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = get_user_model()
        if user.objects.filter(email=email).exists():
            raise forms.ValidationError('사용중인 이메일입니다')
        return email

    def save(self):
        user = super().save()  # User 모델에 먼저 저장
        # print(type(user))
        # dir(user)
        Profile.objects.create(  # Profile model에 create(insert 문과 같음)
            user=user,
            year=self.cleaned_data['year'],
            month=self.cleaned_data['month'],
            day=self.cleaned_data['day'],
            sex=self.cleaned_data['sex'],
        )
        return user


