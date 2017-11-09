from django import forms
from .models import UnknownBoard, UnknowCommnet, GGulTipBoard, ReportBoard, Message

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

class GGulTipBoardCreationForm(forms.ModelForm):

    class Meta:
        model = GGulTipBoard
        fields = ('title', 'user','content','fileContent')

class ReportBoardCreationFrom(forms.ModelForm):

    class Meta:
        model = ReportBoard
        fields = ('title', 'user','content','fileContent')

class MessageCreationFrom(forms.ModelForm):

    class Meta:
        model = Message
        fields = {'title','content'}
