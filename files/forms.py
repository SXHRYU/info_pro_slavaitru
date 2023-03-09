from django import forms
from .models import File
from django.shortcuts import render


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = [
            "filepath",
        ]
