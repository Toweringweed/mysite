#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Mdetail

# Create your views here.
def index(request):
    last_list = Mdetail.objects.order_by('-m_update_douban',)[:5]
    list_cc = []
    for row in last_list:
        list_c = '<li>' + '<a href = "' + row.m_douban_url +'">' + row.m_name + '</a></li>'
        list_cc.append(list_c)
    output = ''.join(list_cc)
    return render(request, 'index.html', {"output": output}, content_type='html')

def test(request):
    return render(request, 'test.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return  HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
