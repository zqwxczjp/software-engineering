#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from django.template import RequestContext
from mainapp.models import News
from django.template.response import TemplateResponse as TR
import urllib
import urllib2
import re

def index(request):
    a=[]
    class Spider:
	    def __init__(self):
		self.siteURL = 'http://today.hit.edu.cn/phb/0.htm'
	 
	    def getPage(self):
		url = self.siteURL
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		return response.read().decode('gbk')
	 
	    def getContents(self):
		page = self.getPage()
		pattern = re.compile("<li><a href='.*?' target='_blank'>.*?</a> ....-..-.. <span style='color:red'>.*?</span></li>",re.S)
		items = re.findall(pattern,page)
		url=[]
		date=[]
		title=[]
		recommend=[]
	    	for i in range(1,10):
			#print items[i]
			#print items[1]
			url_w=re.findall("<a href='.*?'",items[i])
			url.append(url_w[0][9:-1])
			title_w=re.findall("target='_blank'>.*?</a>",items[i])
			title.append(title_w[0][16:-4])
			date_w=re.findall("</a> .*? <",items[1])
			date.append(date_w[0][5:-2])
			recommend_w=re.findall("red'>.*?</span>",items[i])
			recommend.append(recommend_w[0][5:-10])
		return [url,date,title,recommend]
    spider = Spider()
    a=spider.getContents()
    #if News.objects.all[0:9] and News.objects.all[0].recommend_index >int(a[3][0]):
	#con={"b":b}
       # return TR(request,"index.html",con)
    #else:
    add_news=[]
    for i in range(0,9):
	addnews=News(source_url=a[0][i],title=a[2][i],time=a[1][i],recommend_index=a[3][i])
	addnews.save()
	add_news.append(addnews)
    con={"b0":add_news[0],"b1":add_news[1],"b2":add_news[2],"b3":add_news[3],"b4":add_news[4],"b5":add_news[5]}	
    return TR(request,"index.html",con)
# Create your views here.
