from django.urls import path

from . import views

urlpatterns = [
    path('get_ip/', views.get_ip, name='get_ip'),
    path('redirect/', views.redirect, name='redirect'), #  记录信息
]