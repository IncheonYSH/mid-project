from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login  # 로그인 기능을 하는 패키지 함수
from django.contrib.auth import logout as django_logout
from .forms import SignupForm, LoginForm  # forms.py를 생성해서 SignupForm, LoginForm  정의해야 함


# Create your views here.

# def login(request) :
#     return render(request, 'accounts/login.html')

def signup(request):  # 회원가입 요청에 의해 동작
    if request.method == 'POST':  # post 방식으로의 요청만 회원가입 절차를 수행
        # post 방식으로 데이터 전송의 경우에는 네트워크패킷(데이터)
        # 전송할 파일이 없을 경우 request.FILES는 빼도 됨
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():  # form에 유효한 데이터가 있으면 (값을 client가 정상적으로 전송했으면)
            # 사용자가 전송해준 회원가입 정보를 model을 통해서 db에 저장
            user = form.save()  # 회원가입 완료 - forms.py에서 db에 저장되도록 구성해야 함
            return redirect('accounts:login')  # accounts/login 으로 바로 연결
    else:  # GET 방식일 경우
        form = SignupForm()  # 회원가입폼을 다시 출력
    return render(request, 'accounts/signup.html', {'form': form})


def login_check(request):  # 로그인 요청에 의해 동작
    if request.method == "POST":
        form = LoginForm(request.POST)  # post로 넘어온 데이터 객체 반환
        name = request.POST.get('username')  # post로 넘어온 데이터 중 일부 반환
        pwd = request.POST.get('password')

        # user모델과 연동된 db테이블에 사용자가 있는지 확인
        user = authenticate(username=name, password=pwd)

        if user is not None:  # 인증 되었으면
            login(request, user)  # 로그인 진행 - 클라이언트 서버간에 세션을 연결
            return redirect("/")
        else:
            return render(request, 'accounts/login_fail.html')
    else:
        form = LoginForm()  # 잘못된 접근(get방식)
        return render(request, 'accounts/login.html', {"form": form})


def logout(request):
    django_logout(request)  # 기본 로그아웃 기능 사용 - 연결된 세션을 종료
    return redirect("/")