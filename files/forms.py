from django import forms
from .models import File
from django.shortcuts import render


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = [
            'filepath',
        ]

    def get_file_size(request):
        return request.FILES.get('filepath').size
    
    def get_name(self):
        return self.instance.uploaded_file.name
