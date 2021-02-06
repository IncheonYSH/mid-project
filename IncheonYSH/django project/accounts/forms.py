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
    email = forms.EmailField(label='email')
    fullname = forms.CharField(label='fullname')
    year = forms.CharField(label='year')
    # month = forms.CharField(label='month')
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
    day = forms.CharField(label='day')
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
            'fullname',
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
    def clean_year(self):
        year = self.cleaned_data.get('year')
        return year

    def clean_month(self):
        month = self.cleaned_data.get('month')
        return month

    def clean_day(self):
        day = self.cleaned_data.get('day')
        return day

    def clean_sex(self):
        sex = self.cleaned_data.get('sex')
        return sex

    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        return fullname

    def save(self):
        user = super().save()  # User 모델에 먼저 저장
        # print(type(user))
        # dir(user)
        Profile.objects.create(  # Profile model에 create(insert 문과 같음)
            user=user,
            fullname=self.cleaned_data['fullname'],
            year=self.cleaned_data['year'],
            month=self.cleaned_data['month'],
            day=self.cleaned_data['day'],
            sex=self.cleaned_data['sex'],
        )
        return user


