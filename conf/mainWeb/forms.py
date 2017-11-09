from django import forms
from .models import UnknownBoard, UnknowCommnet

class UnknownBoardCreationForm(forms.ModelForm):

    class Meta:
        model = UnknownBoard
        fields = ('title', 'makerUser','content','password')
        widgets = {
        'password': forms.PasswordInput(),
        }

class UnknowCommnetCreationForm(forms.ModelForm):

    class Meta:
        model = UnknowCommnet
        fields = ('user','content')
        labels = {
            "user": "제목",
            "content" : "내용"
        }
