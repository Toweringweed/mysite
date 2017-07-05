#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Mdetail

# Create your views here.
def index(request):
    last_list = Mdetail.objects.order_by('m_update_douban')[:5]
    output = ','.join([p.m_name for p in last_list])
    return HttpResponse(output)

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
