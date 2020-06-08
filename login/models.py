from django.db import models

class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.username
