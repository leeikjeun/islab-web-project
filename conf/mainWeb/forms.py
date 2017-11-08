from django import forms
from .models import UnknownBoard

class UnknownBoardCreationForm(forms.ModelForm):

    class Meta:
        model = UnknownBoard
        fields = ('title', 'makerUser','content','password')
        widgets = {
        'password': forms.PasswordInput(),
    }
