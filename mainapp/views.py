#coding:utf-8
from django.shortcuts import render, RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
from django.template import RequestContext
from mainapp.models import *
from django.template.response import TemplateResponse as TR
#from lib.email import send_active_email
import urllib
import urllib2
import re
import uuid
import time
from django.core.mail import send_mail, EmailMultiAlternatives 
PASSWD_MIN_LENGTH = 3
AGE_DEFAULT = 0
USER_STATE_DEFAULT = -1
USER_STATE_ACTIVE = 1
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
	    	for i in range(1,4):
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
    add_news=[]
    for i in range(0,3):
	addnews=News(source_url=a[0][i],title=a[2][i],time=a[1][i],recommend_index=a[3][i])
	addnews.save()
	add_news.append(addnews)
   # con={"b0":add_news[0],"b1":add_news[1],"b2":add_news[2],"b3":add_news[3],"b4":add_news[4],"b5":add_news[5]}
    

    if request.session:
        print '---------------------session runs--------------------'
    if 'username' in request.session:
        print '----------------------succeed------------------------'
        return render(request, 'loginlater.html', {'username': request.session['username']})
    con={"b0":add_news[0],"b1":add_news[1],"b2":add_news[2]}
    return TR(request,"index.html",con)
    
    #return TR(request,"index.html",{})
#-----------------------------------------------
#激活码计算:邮箱+当前时间
def active_code(email):
    email_code = uuid.uuid5(uuid.NAMESPACE_DNS, email+str(time.time())).hex
    return email_code
    
def send_active_email(username, email):
    if isinstance(email, unicode):
        email = email.encode('utf-8')
    ActiveCode = active_code(email)
    html_content = u'<p>感谢您注册工大圈子，请点击下面的</p><b>激活链接：\
        </b><a href="http://localhost:8000/active/%s/%s">http://hitquanzi/active/%s/%s</a>'\
        % (username, ActiveCode, username, ActiveCode)
    subject, form_email, to = u'激活邮件', 'hitquanzi@sina.com', email
    text_content = u'感谢您注册工大圈子，请点击下面的'
    msg = EmailMultiAlternatives(subject, text_content, form_email, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    #return HttpResponse(u'请查看你注册的信箱完成注册!!')
    return ActiveCode


#-------------------------------------------------
def signup(request):
    error = ''
    if request.method == 'POST':
        p = request.POST
        #输入格式检查, 用户重复检查
        if 'username' in p and not p['username']:
            error = u'请输入用户名！'
        elif 'email' in p and not p['email']:
            error = u'请输入邮箱！'
        elif 'password' in p and not p['password']:
            error = u'请输入密码！'
        elif p['password'] != p['password_confirm']:
            error = u'两次密码不一致！'
        elif len(p['password']) < PASSWD_MIN_LENGTH:
            error = u'密码至少3个字符！'
        elif User.objects.filter(username = p['username']):
            error = u'此用户名\'%s\'已被使用' % p['username']
        elif User.objects.filter(email = p['email']):
            error = u'此邮箱\'%s\'已被使用' % p['email']
        elif False:   #可再加入更多检查
            pass
        else:
            if p['age']:
                try:
                    age = int(p['age'])
                except ValueError:
                    error = u'年龄输入非法字符！'
            else:
                age = AGE_DEFAULT
            if not error:
                #ActiveCode = send_active_email(p['email'])
                newuser = User(\
                    username = p['username'], password = p['password'], \
                    email = p['email'], birthday = '2000-01-01',
                    degree = int('0'),
                    #age = age, \
                    institute = p['institute'], major = p['major'],
                    state = USER_STATE_DEFAULT , 
                    active_code = send_active_email(p['username'], p['email'])
                    )
                newuser.save()
                
                greeting = u'%s, 你好！注册成功~ 请尽快前往您的邮箱激活账户...' % p['username']  
                return HttpResponse(greeting)   #后面跳转到登录后界面，这里先显示成功
    return render(request, 'signup.html', {'error': error}, \
        context_instance=RequestContext(request))



def login(request):
    wrong = ''
    if request.method == 'POST':
        p = request.POST
        user = User.objects.get(username = p['username'])
        if not user:
            wrong = '没有这个用户！'
        elif user.state == USER_STATE_DEFAULT:
            wrong = '此账户还没有激活，请去激活'
        elif user.password != p['password']:
            wrong = '用户名和密码不匹配！'
        else:
            request.session['username'] = p['username']
            print '---------------------create session------------------'
            return render(request, 'loginlater.html', {'username': p['username']}, \
                context_instance=RequestContext(request))
    return render(request, 'index.html', {'tip': wrong}, \
        context_instance=RequestContext(request)) 

    
def logout(request):
    try:
        del request.session['username']
        print '-----------------------session delete------------------------'
    except KeyError:
        print '*********************wrong***********************'
        pass
    home = '/'
    return HttpResponseRedirect(home)

    

def email(request):
    title = u'greeting'
    content = u'first mail from django'
    from_mail = u'hitquanzi@sina.com'
    to_mail = ['89@qq.com'
    ]
    #send_mail(title, content, from_mail, to_mail, fail_silently = False)
    send_active_email('zjp', '254659389@qq.com')
    return HttpResponse('send done!')


def active(request, username, code):
    print username, code
    tip = ''
    user = User.objects.filter(username = username)
    if not user:
        tip = u'无此用户名！'
    else:
        if user[0].state == USER_STATE_ACTIVE:
            tip = u'该用户已激活！'
        elif code == user[0].active_code:
            user.update(state = USER_STATE_ACTIVE, active_code = '')
        else:
            raise Http404
    return render(request, 'ActiveInfo.html', {'tip': tip, 'username': username})
    















