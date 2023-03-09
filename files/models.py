import os
from django.db import models
from django.urls import reverse


# Create your models here.
class File(models.Model):
    name = models.CharField(
        max_length=100,
    )
    filepath = models.FileField(
        # This one here is from python's official docs,
        # File will be saved to MEDIA_ROOT/uploads/2015/01/30.
        upload_to='uploads/%Y/%m/%d/'
    )
    date_uploaded = models.DateField(
        auto_now_add=True,
    )
    file_size = models.PositiveBigIntegerField(
        null=True,
    )

    class Meta:
        ordering = ['-date_uploaded', 'name']

    def __str__(self) -> str:
        return f"{self.name}, {self.id}"

    # def get_absolute_url(self):
    #     return reverse("files-detail", kwargs={"pk": self.pk})
    
    # def extension(self):
    #     _, extension = os.path.splitext(self.file.name)
    #     return extension
    