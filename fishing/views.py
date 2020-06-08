from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Fishes

def get_ip(request):
    all_fishes = Fishes.objects.all().order_by("-created_time")
    paginator = Paginator(all_fishes, 12)

    # 得到合法的 current_page_num
    try:
        current_page_num = int(request.GET.get('page', 1))
        if current_page_num < 1 or current_page_num >paginator.num_pages:
            current_page_num = 1
    except:
        current_page_num = 1

    start_page = current_page_num - 2 if current_page_num - 2 > 0 else 1
    end_page = start_page + 4 if start_page + 4 < paginator.num_pages else paginator.num_pages
    if start_page > end_page - 4:
        start_page = end_page - 4 if end_page - 4 > 0 else 1
    page_range = range(start_page, end_page + 1)

    fishes = paginator.page(current_page_num)
    return render(request, 'get_ip.html', locals())

def redirect(request):
    fish = Fishes()
    fish.ip = request.META.get('REMOTE_ADDR')
    fish.user_agent = request.META.get('HTTP_USER_AGENT')
    fish.refer = request.META.get('HTTP_REFERER')
    fish.x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    fish.save()
    destination = request.GET.get("url")
    print(destination)
    return redirect(destination)