from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError
import django.core.validators
import django.contrib.auth.password_validation
import re
import calendar


class SignupForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title': '특수문자,공백 입력 불가',
    }))
    email = forms.CharField(label='email')
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

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': '필수 입력 필드입니다'}


    def clean_username(self):
        username = self.cleaned_data.get('username')
        alphabet_regex = re.compile(r'[^a-zA-Z0-9]')
        user = get_user_model()
        if alphabet_regex.search(username):
            raise forms.ValidationError('영문 및 숫자만 입력가능합니다')
        if user.objects.filter(username=username).exists():
            raise forms.ValidationError('사용중인 아이디입니다')
        return username

    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        symbol_regex = re.compile(r'[^가-힣a-zA-Z]')
        if symbol_regex.search(fullname) is not None:
            raise forms.ValidationError('특수문자 입력불가')
        return fullname

    def clean_password1(self):
        pw1 = self.cleaned_data.get('password1')
        return pw1

    def clean_password2(self):
        pw1 = self.cleaned_data.get('password1')
        pw2 = self.cleaned_data.get('password2')
        try:
            pcf = django.contrib.auth.password_validation.validate_password(pw1)
        except:
            raise forms.ValidationError('비밀번호 보안 수준이 낮습니다')
        if pw1 != pw2:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다')
        return pw2

    """
    def clean_year(self):
        year = self.cleaned_data.get('year')
        notnum_regex = re.compile(r'[^0-9]')
        if notnum_regex.search(year) is not None:
            raise forms.ValidationError('입력값이 올바르지 않습니다')
        if int(year) < 0:
            raise forms.ValidationError('입력값이 올바르지 않습니다')
        return year

    def clean_month(self):
        month = self.cleaned_data.get('month')
        notnum_regex = re.compile(r'[^0-9]')
        if notnum_regex.search(month) is not None:
            raise forms.ValidationError('입력값이 올바르지 않습니다')
        intmonth = int(month)
        if intmonth < 1 or intmonth > 12:
            raise forms.ValidationError('입력값이 올바르지 않습니다')
        return month
        """

    def clean_day(self):
        day = self.cleaned_data.get('day')
        year = self.cleaned_data.get('year')
        month = self.cleaned_data.get('month')
        if not year:
            raise forms.ValidationError('필수 입력 필드입니다')
        if not month:
            raise forms.ValidationError('필수 입력 필드입니다')
        notnum_regex = re.compile(r'[^0-9]')
        if notnum_regex.search(year) is not None:
            raise forms.ValidationError('입력값이 올바르지 않습니다')
        if int(year) < 0:
            raise forms.ValidationError('입력값이 올바르지 않습니다')
        if notnum_regex.search(month) is not None:
            raise forms.ValidationError('입력값이 올바르지 않습니다')
        intmonth = int(month)
        if intmonth < 1 or intmonth > 12:
            raise forms.ValidationError('입력값이 올바르지 않습니다')
        if notnum_regex.search(day) is not None:
            raise forms.ValidationError('입력값이 올바르지 않습니다')
        end_day = calendar.monthrange(int(year), int(month))[1]
        if int(day) < 1 or int(day) > end_day:
            raise forms.ValidationError('입력값이 올바르지 않습니다')
        return day

    def clean_sex(self):
        sex = self.cleaned_data.get('sex')
        if sex != 'M' and sex != 'F':
            raise forms.ValidationError('유효하지 않은 값입니다')
        return sex

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = get_user_model()
        try:
            mch = django.core.validators.validate_email(email)
        except:
            raise forms.ValidationError('입력값이 올바르지 않습니다')
        if user.objects.filter(email=email).exists():
            raise forms.ValidationError('사용중인 이메일입니다')
        return email

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