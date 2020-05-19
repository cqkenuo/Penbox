from django.shortcuts import render

# Create your views here.

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    get_ip= ip() #imported class from model
    get_ip.ip_address= ipaddress
    get_ip.pub_date = datetime.date.today() #import datetime
    get_ip.save()