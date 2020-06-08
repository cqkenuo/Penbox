from django.db import models

class Fishes(models.Model):

    ip = models.GenericIPAddressField(verbose_name="ip")
    user_agent = models.CharField(max_length=128, verbose_name="UA", null=True, blank=True)
    refer = models.CharField(max_length=128, verbose_name="refer", null=True, blank=True)
    x_forwarded_for = models.CharField(max_length=128, verbose_name="x_forwarded_for", null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="访问时间")
