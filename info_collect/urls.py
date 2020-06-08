from django.urls import path

from . import views

urlpatterns = [
    path('subdomain', views.subdomain, name='subdomain'),
]