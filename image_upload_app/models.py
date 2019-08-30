from django.db import models
from .validators import validate_file_extension, validate_image


class Picture(models.Model):
    title = models.CharField(max_length=30)
    cover = models.ImageField(upload_to="images/", null=True, blank=True,
                              validators=[validate_file_extension, validate_image])
    Description = models.TextField(max_length=1000, null=False, default="")

    def __str__(self):
        return self.title
