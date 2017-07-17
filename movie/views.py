from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Mdetail

def index(request):
    last_list = Mdetail.objects.order_by('-m_update_douban')[:5]

    # list_cc = []
    # for row in last_list:
    #     list_c = '<li>' + '<a href = "' + row.m_douban_url +'">' + row.m_name + '</a></li>'
    #     list_cc.append(list_c)
    # output = ''.join(list_cc)
    return render(request, 'index.html', {"last_list": last_list}, content_type='html')

def detail(request, m_id):
    detail = get_object_or_404(Mdetail, m_id=m_id)
    # detail = Mdetail.objects.get(m_id=m_id)
    return render(request, 'detail.html', {"detail": detail}, content_type='html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
