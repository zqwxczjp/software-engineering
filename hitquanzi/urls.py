#coding:utf-8
"""hitquanzi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mainapp.views import *
import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name = 'home'),
    url(r'^signup/$', signup, name = 'signup'), #注册
    url(r'^login/$', login),
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^email/$', email),    #just a test
    url(r'^news_page/$', news_page),
    url(r'^active/(?P<username>[a-zA-Z0-9_]{3,50})/(?P<code>\w+)$', active),
    
    #url(r'^css/(?P<path>.*)', 'django.views.static.serve',
    #    {'document_root': settings.CSS_DIR}),
]
