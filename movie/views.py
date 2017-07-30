from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Mdetail, Marea
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    last_list = Mdetail.objects.order_by('-m_update_douban')[:5]
    last_china = Mdetail.objects.filter(Q(m_year__m_year="2000"), Q(m_area__m_area__contains="大陆") | Q(m_area__m_area__contains="香港"))[:5]
    # list_cc = []
    # for row in last_list:
    #     list_c = '<li>' + '<a href = "' + row.m_douban_url +'">' + row.m_name + '</a></li>'
    #     list_cc.append(list_c)
    # output = ''.join(list_cc)
    return render(request, 'index.html', {"last_list": last_list, "last_china": last_china})

def detail(request, m_id):
    detail = get_object_or_404(Mdetail, m_id=m_id)
    return render(request, 'detail.html', {"detail": detail})

def pagination(p, t, arg, cur_num):
    page_range = p.page_range
    num_page = p.num_pages
    page = []
    if num_page <= 12:
        page = page_range
    else:
        if cur_num <= 10:
            page = range(1, 13)
        else:
            show_start = cur_num - 10
            show_end = cur_num + 2 if cur_num+1 <= num_page else cur_num
            page = range(show_start, show_end)
    page_show = []
    for i in page:
        i_show = r'<a href="%d">[%d]</a>' % (i, i) if i == cur_num else r'<a href="%d">%d</a>' % (i, i)
        page_show.append(i_show)

    page_middle = ' &nbsp;'.join(i for i in page_show)
    page_index = r'<a href="1">首页</a>'
    page_end = r'<a href="%d">末页</a>' % num_page
    page_list = p.page(cur_num)
    next_num = page_list.next_page_number() if page_list.has_next() else -1
    pre_num = page_list.previous_page_number() if page_list.has_previous() else -1
    page_next = r'<a href="%d">下一页</a>' % next_num if next_num != -1 else ''
    page_pre = r'<a href="%d">上一页</a>' % pre_num if pre_num != -1 else ''
    page_sum = r'共%d页 %d条' % (p.num_pages, p.count)
    page = ' &nbsp; &nbsp;'.join([page_index, page_pre, page_middle, page_next, page_end, page_sum])
    return page

def movie_list(request, t, arg, cur_num):
    movie_list = ''
    if t == 'area':
        movie_list = Mdetail.objects.filter(m_area__m_area__contains=arg).order_by('-m_year__m_year').order_by('-m_first_play')
    if t == 'tag':
        movie_list = Mdetail.objects.filter(m_tag__m_tag__contains=arg).order_by('-m_year__m_year').order_by('-m_first_play')

    p = Paginator(movie_list, 20)
    page_list = p.page(cur_num)
    cur_num = int(cur_num)
    show = pagination(p, t, arg, cur_num)
    return render(request, 'movie_list.html', {
        "page_list": page_list,
        "page": show

    })

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
