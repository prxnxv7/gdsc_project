from django.db import models
from django.utils import timezone

class UploadImage(models.Model):
    name = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=10,default="")
    image = models.ImageField(upload_to='images/')
    comment = models.TextField(max_length=150)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name