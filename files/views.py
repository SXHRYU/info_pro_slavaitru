from django import forms
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .forms import UploadFileForm
from .models import File


class FilesUpload(CreateView):
    template_name = "files/upload.html"
    form_class = UploadFileForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.name = self.request.FILES["filepath"].name
        form.instance.file_size = self.request.FILES["filepath"].size
        form.instance.data_types = form.instance.assign_file_data_types()

        # form.cleaned_data["name"] = self.request.FILES['filepath'].name
        # form.cleaned_data["file_size"] = self.request.FILES['filepath'].size
        # form.cleaned_data["data_types"] = form.instance.assign_data_types()
        return super().form_valid(form)
