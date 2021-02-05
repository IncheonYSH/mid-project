from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm) : # ModelForm - model을 기준으로 form 생성
    class Meta:
        model = User
        fields = ["username","password"]

class SignupForm(UserCreationForm) :
    # 문자 입력 필드를 생성 : 사용자명 입력칸 형태로 만들어짐
    username = forms.CharField(label='사용자명', widget=forms.TextInput(attrs={
        'pattern' : '[a-zA-Z0-9]+', # 생성되는 username은 대소문자와 숫자로만
        'title' : '특수문자, 공백 입력 불가'
    }))
    nickname = forms.CharField(label='닉네임') # 닉네임 입력 필드 생성
    picture = forms.ImageField(label='프로필 사진',required=False) # required = False -> 입력 안해도 된다는뜻
    # form과 관련된 class는 반드시 내부에 meta 클래스를 갖고 있어야 함
    class Meta(UserCreationForm.Meta) : # 상위 클래스 상속 받아 생성
        fields = UserCreationForm.Meta.fields + ('email',)
    # 장고는 UserCreationForm을 제공하며, 해당 form안에 username, password1, password2의 필수 필드와
    # email 등 선택 필드가 포함되어 있음 - Meta 구성해 놓으면 해당 필드를 그대로 사용 할 수 있음
    
    # 입력 내용의 유효성검사가 반드시 필요함
    # UserCreationForm이 제공 clean_필드명 메서드를 이용하면 간단하게 유효성 검사가 가능
    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        # db에 동일한 nickname이 있는지 확인
        if Profile.objects.filter(nickname = nickname).exists() :
            raise forms.ValidationError('이미 존재하는 닉네임입니다.') # 에러 발생
        return nickname

    def clean_email(self):
        email=self.cleaned_data.get('email')
        User = get_user_model() # user모델 전부 가져와서 User변수에 저장 - user 모델은 장고가 내부적으로 제공하는 모델
        if User.objects.filter(email=email).exists() : # email이 존재하면
            raise forms.ValidationError('사용중인 이메일입니다.')
        return email
    
    def clean_picture(self): # 파일이 있는지 확인
        picture = self.cleaned_data.get('picture')
        if not picture :
            picture = None # 프로필 사진
        return picture
    
    def save(self):
        user=super().save() # User 모델에 먼저 저장
        Profile.objects.create( # Profile model에 create(insert 문과 같음)
            user=user,
            nickname = self.cleaned_data['nickname'],
            picture = self.cleaned_data['picture'],
        )
        return user

