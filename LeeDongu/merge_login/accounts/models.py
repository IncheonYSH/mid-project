from django.db import models
from django.conf import settings    # 인증 관련 패키지 사용을 위한 import
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.


# 파일 저장 경로 설정 함수
def user_path(instance, filename):
    # instance : photo
    # filename : 업로드 된 파일 명
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)  # 무작위로 생성 된 8문자를 하나의 문자열로 생성
    extension = filename.split('.')[-1]  # 사용자가 올린 이밎파일명의 파일 확장자 선택
    return 'account/{}/{}.{}'.format(instance.user.username, pid, extension)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField('별명', max_length=20, unique=True)
    picture = ProcessedImageField(upload_to=user_path,  # upload 될 공간을 지정 (user_path라는 함수를 따로 구성해서 경로 생성 할 예정)
                                  processors=[ResizeToFill(150, 150)],  # upload된 image size를 150*150으로 조정
                                  format='JPEG',  # image 형식 설정
                                  options={'quality': 90},  # image의 품질 설정
                                  blank=True)
    about = models.CharField(max_length=300, blank=True)
    Gender = (
        ('선택암함', '선택안함'),
        ('여성', '여성'),
        ('남성', '남성'),
    )  # 일반 변수 - db 필드 사용되지 않음

    gender = models.CharField('성별(선택사항)',
                              max_length=10,
                              choices=Gender,
                              default='N')

    def __str__(self):
        return self.nickname
