from django import forms
from .models import MainModel
class MainForm(forms.ModelForm):
    class Meta:
        model = MainModel
        fields = ["header", "image", "description", "status"]