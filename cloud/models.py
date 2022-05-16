from datetime import datetime

from django.db import models
# from djongo import models
from django.utils import timezone
from django.conf import settings


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30, unique=True)
    phone_num = models.CharField(max_length=15, blank=True)


class FileDetailInfo(models.Model):
    file_title = models.CharField(max_length=50)
    file_upload = models.DateField(timezone.now)
    file_url = models.FileField(upload_to='directory/')
    owner_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.file_title


class Comment(models.Model):
    file_detail = models.ForeignKey(FileDetailInfo, related_name='comments', on_delete=models.CASCADE)
    comment_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_date = models.DateField(default=timezone.now)
    comment_text = models.TextField()

