from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import File


class FilesUpload(CreateView):
    template_name = "files/upload.html"
    form_class = UploadFileForm

    def form_valid(self, form):
        form.instance.name = self.request.FILES["filepath"].name
        form.instance.file_size = self.request.FILES["filepath"].size
        form.instance.data_types = form.instance.assign_file_data_types()
        
        file = form.save()
        return HttpResponseRedirect(reverse("files-detail", args=(file.pk,)))


class FilesDetail(DetailView):
    template_name = "files/detail.html"
    model = File

    context_object_name = "model"

class FilesUpdate(UpdateView):
    template_name = "files/update.html"
    model = File
    fields = ("data_types",)

    context_object_name = "model"

    def form_valid(self, form):
        file = form.save()
        return HttpResponseRedirect(reverse("files-detail", args=(file.pk,)))
