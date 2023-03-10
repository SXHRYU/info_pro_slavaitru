import os
from django.db import models
from django.urls import reverse
from assigner import TypeAssigner


# Create your models here.
class File(models.Model):
    name = models.CharField(
        max_length=100,
    )
    filepath = models.FileField(
        # This one here is from python's official docs,
        # File will be saved to MEDIA_ROOT/uploads/2015/01/30.
        upload_to="uploads/%Y/%m/%d/"
    )
    date_uploaded = models.DateField(
        auto_now_add=True,
    )
    file_size = models.PositiveBigIntegerField()
    data_types = models.JSONField()

    class Meta:
        ordering = ["-date_uploaded", "name"]

    def assign_file_data_types(self):
        t = TypeAssigner()
        types = []
        for data in self.filepath.file.readline().decode().split("\t"):
            if data[-1] == "\n":
                data = data[:-1]
                if data[-1] == "\r":
                    data = data[:-1]
            types.append(t.assign_data_type(data).verbose_name)
        return types

    def __str__(self) -> str:
        return f"Файл '{self.name}' ID: {self.pk}"

    def __repr__(self) -> str:
        return f"models.{super().__str__()}"

    def get_absolute_url(self):
        return reverse("files-detail", kwargs={"pk": self.pk})
