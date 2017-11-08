from django import forms
from .models import TestBoard

class TestBoardCreationForm(forms.ModelForm):

    class Meta:
        model = TestBoard
        fields = ('title', 'makerUser','content','fileContent')
