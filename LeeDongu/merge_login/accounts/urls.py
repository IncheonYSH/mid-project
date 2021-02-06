from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/',signup, name='signup'), # 회원가입을 위한 url
    path('login/',login_check,name='login'), # 로그인 요청을 위한 url
    path('logout/',logout, name='logout'), # 로그아웃 요청을 위한 url
]