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
    url(r'^$', hello, name = 'hello'),
    url(r'^home/(?P<username>[a-zA-Z0-9_]{3,50})/$', index, name = 'home'),
    url(r'^signup/$', signup, name = 'signup'), #注册
    url(r'^login/$', login),
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^email/$', email),    #just a test
    url(r'^news_page/$', news_page),
    url(r'^self_pagehehe/$', self_pagehehe),
    url(r'^course/(?P<username>[a-zA-Z0-9_]{3,50})/$', course, name = 'course'),
    url(r'^news_page/(?P<username>[a-zA-Z0-9_]{3,50})/(?P<url>.+)$', news_page,name='news_paget'),
    url(r'^self_pagehehe/(?P<username>[a-zA-Z0-9_]{3,50})/(?P<url>.+)$', self_pagehehe,name="self_pagehehe"), 
    url(r'^replays/$', replays),
    url(r'^active/(?P<username>[a-zA-Z0-9_]{3,50})/(?P<code>\w+)$', active),
    url(r'^friend/(?P<username>[a-zA-Z0-9_]{3,50})/$', friend, name = 'friendt'),
    url(r'^self_page/(?P<username>[a-zA-Z0-9_]{3,50})/$', self_page, name = 'self_page'),
    url(r'^addfriend/(?P<username>[a-zA-Z0-9_]{3,50})/(?P<friendID>\d+)/$', addfriend, name = 'addfriend'),
    url(r'^addfriendconfirm/(?P<username>[a-zA-Z0-9_]{3,50})/(?P<friendID>\d+)/$',\
		addfriendconfirm, name = 'addfriendconfirm'),
	url(r'^sendmesg/(?P<username>[a-zA-Z0-9_]{3,50})/(?P<friendID>\d+)/$', SendMesgx, name = 'SendMesg'),
    url(r'^markread/(?P<mesgid>\d+)/$', MarkRead, name = 'MarkRead'),
    url(r'^upload_img/$', UploadImg, name = 'upload_img'),
    url(r'^userinfo/(?P<username>[a-zA-Z0-9_]{3,50})/$', UserInfo, name = 'userinfo'),
    url(r'^css/(?P<path>.*)', 'django.views.static.serve',\
        {'document_root': settings.CSS_DIR}),
    url(r'^img/(?P<path>.*)', 'django.views.static.serve',\
        {'document_root': settings.IMG_DIR}),
    url(r'^forwardcourse/(?P<username>[a-zA-Z0-9_]{3,50})/(?P<url>.+)$', forwardcourse,name="forwardcourse"), 
]
