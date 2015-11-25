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
from lxml import etree
import urllib2
import codecs
from django.core.mail import send_mail, EmailMultiAlternatives 
PASSWD_MIN_LENGTH = 3
AGE_DEFAULT = 0
USER_STATE_DEFAULT = -1
USER_STATE_ACTIVE = 1
def index(request):
    requesth = urllib2.Request("http://today.hit.edu.cn/phb/0.htm")
    response = urllib2.urlopen(requesth)

    selector=etree.HTML(response.read().decode('gb2312'))

    title=selector.xpath("//div[@class='charbox_content']/ol/li/a/text()")
    time=selector.xpath("//div[@class='charbox_content']/ol/li/text()")
    recommend_index=selector.xpath("//div[@class='charbox_content']/ol/li/span/text()")
    source_url=selector.xpath("//div[@class='charbox_content']/ol/li/a/@href")
    add_news=[]
    for i in range(0,11):
	addnews=News(source_url=source_url[i],title=title[i],time=time[i],recommend_index=recommend_index[i])
	add_news.append(addnews)
 

    if request.session:
        print '---------------------session runs--------------------'
    if 'username' in request.session:
        print '----------------------succeed------------------------'
        return render(request, 'loginlater.html', {'username': request.session['username'],"b1":add_news[5],"b2":add_news[6],"b3":add_news[7],"b4":add_news[8],"b5":add_news[9],"b0":add_news[10]})
    
    con={"b0":add_news[0],"b1":add_news[1],"b2":add_news[2],"b3":add_news[3],"b4":add_news[4],"b5":add_news[5]}
    return TR(request,"index.html",con)
    
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

def email(request):
    'just a test'
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
            user.update(state = USER_STATE_ACTIVE)
        else:
            raise Http404
    return render(request, 'ActiveInfo.html', {'tip': tip, 'username': username})
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
    requesth = urllib2.Request("http://today.hit.edu.cn/phb/0.htm")
    response = urllib2.urlopen(requesth)

    selector=etree.HTML(response.read().decode('gb2312'))

    title=selector.xpath("//div[@class='charbox_content']/ol/li/a/text()")
    time=selector.xpath("//div[@class='charbox_content']/ol/li/text()")
    recommend_index=selector.xpath("//div[@class='charbox_content']/ol/li/span/text()")
    source_url=selector.xpath("//div[@class='charbox_content']/ol/li/a/@href")
    add_news=[]
    for i in range(5,11):
	addnews=News(source_url=source_url[i],title=title[i],time=time[i],recommend_index=recommend_index[i])
	add_news.append(addnews)
    if request.method == 'POST':
        p = request.POST
        user = User.objects.filter(username = p['username'])
        if not user:
            wrong = '没有这个用户！'
        elif user[0].state == USER_STATE_DEFAULT:
            wrong = '此账户还没有激活，请去激活'
        elif user[0].password != p['password']:
            wrong = '用户名和密码不匹配！'
        else:
            request.session['username'] = p['username']
            print '---------------------create session------------------'
            return render(request, 'loginlater.html', {'username': p['username'],"b0":add_news[0],\
		"b1":add_news[1],"b2":add_news[2],"b3":add_news[3],"b4":add_news[4],"b5":add_news[5]}, \
                context_instance=RequestContext(request))
    return render(request, 'index.html', {'tip': wrong,"b0":add_news[0],\
		"b1":add_news[1],"b2":add_news[2],"b3":add_news[3],"b4":add_news[4],"b5":add_news[5]}, \
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

def news_page(requestl):
    url=requestl.GET['url']
    realurl='http://today.hit.edu.cn'+ url
    request = urllib2.Request(realurl)
    response = urllib2.urlopen(request)
    selector=etree.HTML(response.read().decode('gbk'))
    contents=selector.xpath("//div[@id='page_main']")
    info=contents[0].xpath('string(.)')   
    return TR(requestl,"新闻页.html",{"info":info}) 

def self_page(request,username):
    if not 'username' in request.session:
        raise Http404
#显示自己的好友
    user = User.objects.filter(username = username)
    #查找为空，Http404
    if not user:
        raise Http404
    user = user[0]
    news = ForwardNews.objects.filter(user = user)
 
    return TR(request,"self_page.html",{'username':username,'news':news})

def self_pagehehe(request):
    newsadd=request.GET['new']
    username=request.GET['username']
    userzu=User.objects.filter(username = username)
    user=userzu[0]
    newnews=ForwardNews(user=user,title=newsadd)
    newnews.save()
    news = ForwardNews.objects.filter(user = user)
 
    return TR(request,"self_page.html",{'username':username,'news':news})
    

def friend(request, username):
#没有登录，Http404
    if not 'username' in request.session:
        raise Http404
#显示自己的好友
    user = User.objects.filter(username = username)
    #查找为空，Http404
    if not user:
        raise Http404
    user = user[0]
    part1 = Friends.objects.filter(userID = user.id)
    part2 = Friends.objects.filter(friendID = user.id)
    friends = []
    if part1:
        for f in part1:
            friends.append(User.objects.get(id = f.friendID))
    elif part2:
        for f in part2:
            friends.append(User.objects.get(id = f.friendID))
    else:
        pass
#搜索好友
    Results = None
    Tip = None
    HasSearch = False
    SearchChar = ''
    if 'SearchChar' in request.GET:
        SearchChar = request.GET['SearchChar']
        if SearchChar:
            Results = User.objects.filter(username__icontains = SearchChar)
            HasSearch = True
    return TR(request, 'freinds.html',\
        {'username':username, 'friends':friends,\
        'Results':Results,'Tip':Tip, 'SearchChar':SearchChar,\
        'HasSearch':HasSearch })

def addfriend(request, username, friendID):
    se = request.session
    FdName = ''
    if not 'username' in se:#没有登录
        raise Http404
    if se['username'] != username:#不是本人操作
        raise Http404
    user = User.objects.filter(username = username)
    if user:
        user = user[0]
        if user.id > friendID:#前面存放id较小的
            smallID = friendID
            bigID = user.id
        else:
            smallID = user.id
            bigID = friendID
        if not Friends.objects.filter(userID = smallID, friendID = bigID):
            Fds = Friends(userID = smallID, friendID = bigID)
            Fd = User.objects.filter(id = friendID)
            if Fd:
                Fd = Fd[0]
                FdName = Fd.username
            Fds.save()
        else:
            raise Http404
    else:
        raise Http404
    #url = '/friend/%s/' % username
    return TR(request, 'AddFriendTimer.html',\
        {'FdName': FdName,'username': username})











