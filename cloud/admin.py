from django.contrib import admin

# Register your models here.
from cloud.models import FileDetailInfo, UserInfo, Comment

admin.site.register(FileDetailInfo)

admin.site.register(UserInfo)

admin.site.register(Comment)
