from django import forms
from .models import UnknownBoard, UnknowCommnet

class UnknownBoardCreationForm(forms.ModelForm):

    class Meta:
        model = UnknownBoard
        fields = ('title', 'makerUser','content','password')
        widgets = {
        'password': forms.PasswordInput(),
        }
        labels = {
            "title": "제목",
            "makerUser" : "별명",
            "content" : "내용",
            "password" : "비밀번호"
        }

class UnknowCommnetCreationForm(forms.ModelForm):

    class Meta:
        model = UnknowCommnet
        fields = ('user','content')
        labels = {
            "user": "제목",
            "content" : "내용"
        }
