from django import forms
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .forms import UploadFileForm
from .models import File


class FilesUpload(CreateView):
    template_name = 'files/upload.html'
    form_class = UploadFileForm
    success_url = '/'
