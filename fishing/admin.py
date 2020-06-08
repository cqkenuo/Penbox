from django.contrib import admin

from .models import Fishes


class Fish(admin.ModelAdmin):
    list_display = ('ip', 'user_agent', 'refer', "x_forwarded_for", 'created_time')

admin.site.register(Fishes, Fish)