from django.contrib import admin
from .models import Profile
# Register your models here.

# admin 계정을 통해 db 데이터 입출력

# admin 페이지에 Profile 데이터를 저장할 수 있도록 구성
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin) :
    list_display = ['id','nickname','user']
    list_display_links = ['nickname','user']
    search_fields = ['nickname']
