"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from movie import views as movie_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^detail/(\d+)/$', movie_view.detail, name='detail'),
    url(r'^movie_list/(\w+)/(\w+)/(\d+)', movie_view.movie_list, name='movie_list'),
    url(r'^$', movie_view.index),
    url(r'^add/$', movie_view.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', movie_view.add2, name='add2')
]
