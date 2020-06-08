from django.contrib import admin
from . import models

# 将User注册到admin页面
admin.site.register(models.User)