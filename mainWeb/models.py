from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os

# Create your models here.


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 기본 유저 정보
    school_num = models.CharField(max_length=30, blank=True) # 학번
    phone_num = models.CharField(max_length=500, blank=True) # 핸드폰 번호
    birth_date = models.DateField(null=True, blank=True) # 생일
    authority = models.IntegerField() # 권한
    email = models.CharField(max_length=40, blank=True) # 메일

class UnknowNameBoard(models.Model):
    board_num = models.AutoField(primary_key=True) # 계시판 번호
    title = models.CharField(max_length=100, blank=False) # 제목
    content = models.TextField(max_length=500, blank=True) # 내용
    password = models.CharField(max_length=30, blank=True) # 비밀번호
    date = models.DateField(null=False) # 날짜
    nick_name = models.CharField(max_length=30,blank=False) # 별명

 class ProffessorData(models.Model):
    name = models.CharField(max_length=100, blank=False)
    profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True) # 메일

    #메시지 만드는 url 나중에 구현하면서 할꺼 귀찮;;
    #https://docs.djangoproject.com/ko/1.11/ref/contrib/messages/
