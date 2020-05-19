from django.db import models

class Fishes(models.Model):

    IP = models.GenericIPAddressField(verbose_name="IP")
    user_agent = models.CharField(max_length=128, verbose_name="UA")
    refer = models.CharField(max_length=128, verbose_name="refer")
    x_forwarded_for = models.CharField(max_length=128, verbose_name="x_forwarded_for")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="访问时间")
