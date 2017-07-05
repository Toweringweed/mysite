from django.shortcuts import render
from django.http import HttpResponse
from .models import Mdetail

# Create your views here.
def index(request):
    last_list = Mdetail.objects.order_by('m_update_douban')[:5]
    output = ','.join([p.m_name for p in last_list])
    return HttpResponse(output)

