from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    fields = ['filepath']

admin.site.register(File, FileAdmin)
