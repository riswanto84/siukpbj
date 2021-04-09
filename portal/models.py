from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Banner(models.Model):
    description = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Pengumuman(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PengumumanFiles(models.Model):
    pengumuman = models.ForeignKey(Pengumuman, on_delete=models.CASCADE)
    files = models.FileField(
        max_length=255, upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.pengumuman.title
