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
from mylib import AddFriendReq
from PIL import Image
PASSWD_MIN_LENGTH = 3
AGE_DEFAULT = 0
USER_STATE_DEFAULT = -1
USER_STATE_ACTIVE = 1
REQ_DIR_L_R = -1
REQ_DIR_R_L = 1
REQ_AGREED = 0

def hello(request):
    return TR(request, "sign_in&up.html")

def index(request, username):
    if 'username' in request.session:
        requesth = urllib2.Request("http://today.hit.edu.cn/phb/0.htm")
        response = urllib2.urlopen(requesth)

        selector=etree.HTML(response.read().decode('gb2312'))

        title=selector.xpath("//div[@class='charbox_content']/ol/li/a/text()")
        time=selector.xpath("//div[@class='charbox_content']/ol/li/text()")
        recommend_index=selector.xpath("//div[@class='charbox_content']/ol/li/span/text()")
        source_url=selector.xpath("//div[@class='charbox_content']/ol/li/a/@href")
        add_news=[]
        add_news_base=[]
        all_news=News.objects.all()	
        for i in range(11):
            addnews=News(source_url=source_url[i],title=title[i],time=time[i],recommend_index=recommend_index[i])
            flag=False
            for j in range(len(all_news)):
                if addnews.title==all_news[j].title:
                    flag=True
                    break
            if flag==False:
                addnews.save()
            add_news.append(addnews)

        all_news=News.objects.all()
        if all_news == None:
            for i in range(len(add_news)):       
                add_news[i].save()
        return render(request, 'loginlater.html', {'username': username,"b0":add_news[0],\
		"b1":add_news[1],"b2":add_news[2],"b3":add_news[3],"b4":add_news[4],"b5":add_news[5]}, \
                context_instance=RequestContext(request))
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
    return render(request, 'sign_in&up.html', {'error': error}, \
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
    add_news_base=[]
    all_news=News.objects.all()	
    for i in range(11):
	addnews=News(source_url=source_url[i],title=title[i],time=time[i],recommend_index=recommend_index[i])
	flag=False
	for j in range(len(all_news)):
	    if addnews.title==all_news[j].title:
		flag=True
		break
	if flag==False:
	    addnews.save()
	add_news.append(addnews)

    all_news=News.objects.all()	
    if all_news == None:
        for i in range(len(add_news)):       
            add_news[i].save()	
        

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
            #print '---------------------create session------------------'
            return render(request, 'loginlater.html', {'username': p['username'],"b0":add_news[0],\
		"b1":add_news[1],"b2":add_news[2],"b3":add_news[3],"b4":add_news[4],"b5":add_news[5]}, \
                context_instance=RequestContext(request))
    return render(request, 'sign_in&up.html', {'tip': wrong},\
        context_instance=RequestContext(request)) 

    
def logout(request):
    try:
        del request.session['username']
        #print '-----------------------session delete------------------------'
    except KeyError:
        #print '*********************wrong***********************'
        pass
    home = '/'
    return HttpResponseRedirect(home)

def news_page(requestl,username,url):
    if not 'username' in requestl.session:
        raise Http404
    user = User.objects.filter(username = username)
    if not user:
        raise Http404
    view_news=News.objects.filter(source_url=url)[0]
    replays = NewsComment.objects.filter(Newsinfo=view_news)
    realurl='http://today.hit.edu.cn'+ url
    request = urllib2.Request(realurl)
    response = urllib2.urlopen(request)
    selector=etree.HTML(response.read().decode('gbk'))
    contents=selector.xpath("//div[@id='page_main']")
    info=contents[0].xpath('string(.)')   
    return TR(requestl,"新闻页test.html",{"view_news":view_news,"info":info,"username":username,"replays":replays}) 

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

def self_pagehehe(request,username,url):
    if not 'username' in request.session:
        raise Http404
    userzu = User.objects.filter(username = username)
    if not userzu:
        raise Http404
    user=userzu[0]
    the_news=News.objects.filter(source_url=url)[0]
    
    newnews=ForwardNews(user=user,title=the_news.title,url=the_news.source_url,time=the_news.time)
    newnews.save()  #应该是这个model的url和time不能为空
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
    mylist = []
    if part1:
        for f in part1:
            user_t = User.objects.get(id = f.friendID)
            friends.append(User.objects.get(id = f.friendID))
            mylist.append(AddFriendReq(user_t.username, f.friendID, f.ReqDirection))
    elif part2:
        for f in part2:
            user_t = User.objects.get(id = f.userID)
            friends.append(User.objects.get(id = f.userID))
            mylist.append(AddFriendReq(user_t.username, f.userID, -f.ReqDirection))
    else:
        pass
    #print mylist[0].username
    Info = []
    Mesgs = SendMesg.objects.filter(userTo=user.id, HasRead=False)
    for mesg in Mesgs:
        tmp = [mesg, User.objects.filter(id=mesg.userFrom)[0]]
        Info.append(tmp)
#搜索用户
    Results = None
    Tip = None
    HasSearch = False
    SearchChar = ''
    if 'SearchChar' in request.GET:
        SearchChar = request.GET['SearchChar']
        if SearchChar:
            Results = User.objects.filter(username__icontains = SearchChar)
            HasSearch = True
    return TR(request, 'friends.html',\
        {'username':username, \
        'myself':user,\
        'friends':friends,'mylist':mylist, 'Info':Info,\
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
        ReqDir = 0
        if user.id > friendID:#前面存放id较小的
            smallID = friendID
            bigID = user.id
            ReqDir = REQ_DIR_R_L
        else:
            smallID = user.id
            bigID = friendID
            ReqDir = REQ_DIR_L_R
        if not Friends.objects.filter(userID = smallID, friendID = bigID):
            Fds = Friends(userID = smallID, friendID = bigID, ReqDirection = ReqDir)
            Fds.save()
        else:
            raise Http404
    else:
        raise Http404
    #url = '/friend/%s/' % username
    urlx = 'http://localhost:8000/friend/%s' % username
    display = '请等待%s确认 ^_^' % FdName
    return TR(request, 'WaitInfo.html',\
        {'urlx':urlx, 'display':display})

def addfriendconfirm(request, username, friendID):
    if not 'username' in request.session:
        raise Http404
    user = User.objects.filter(username = username)[0]
    part1 = Friends.objects.filter(userID = user.id, friendID = friendID)
    part2 = Friends.objects.filter(userID = friendID, friendID = user.id)
    if part1:
        part1.update(ReqDirection = REQ_AGREED)
    elif part2:
        part2.update(ReqDirection = REQ_AGREED)
    else:
        raise Http404
    urlstr = '/friend/%s' % username
    return HttpResponseRedirect(urlstr)


def SendMesgx(request, username, friendID):
    if not 'username' in request.session:
        raise Http404
    userFromt = User.objects.filter(username = username)[0]
    userTot = User.objects.filter(id = friendID)[0]
    if not userFromt or not userTot:
        raise Http404
    Tips = ''
    if request.method == 'POST':
        content = request.POST['content']
        if not content:
            Tips='必须输入至少一个字符!'
        else:
            print userFromt.id 
            print userTot.id
            new_mesg = SendMesg(userTo=userTot.id,\
                userFrom=userFromt.id, Content=content, HasRead=False)
            new_mesg.save()
            urlx = 'http://localhost:8000/sendmesg/%s/%d/' % (userFromt.username, userTot.id)
            display = '发送成功！'
            return TR(request, 'WaitInfo.html',\
                {'urlx':urlx, 'display':display})
    return render(request, 'SendMesg.html',\
        {'Tips':Tips, 'userfrom':userFromt, \
        'userto':userTot,'username':userFromt.username,\
        }, \
        context_instance=RequestContext(request))


def MarkRead(request, mesgid):
    if not 'username' in request.session:
        raise Http404
    mesg = SendMesg.objects.filter(id=mesgid)
    mesg.update(HasRead = True)
    urlstr = '/friend/%s' % User.objects.filter(id=mesg[0].userTo)[0].username
    return HttpResponseRedirect(urlstr)
    
def UploadImg(request):
    if request.method == 'POST':
        rp = request.POST
        imgfile = request.FILES['image']
        try:
            img = Image.open(imgfile)
            #img.thumbnail((200,200),Image.ANTIALIAS)
            img = img.resize((200,200))
            path = './img/%s_icon.jpg' % rp['username']#, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
            img.save(path, "jpeg")
        except Exception, e:
            return HttpResponse("Error: %s" % e)
    return render(request, 'UploadImg.html',{},\
        context_instance=RequestContext(request))
        
        
def UserInfo(request, username):
    if not 'username' in request.session:
        raise Http404
    tip = ''
    myself = User.objects.filter(username=username)
    if request.method == 'POST':
        p = request.POST
        myself.update(institute=p['institute'], major=p['major'], \
            birthday=p['birthday'])
        if request.FILES:
            imgfile = request.FILES['icon']
            try:
                img = Image.open(imgfile)
                #img.thumbnail((200,200),Image.ANTIALIAS)
                img = img.resize((200,200))
                path = './img/%s_icon.jpg' % username#, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
                img.save(path, "jpeg")
            except Exception, e:
                return HttpResponse("Error: %s" % e)
        urlx = 'http://localhost:8000/userinfo/%s/' % username
        display = '修改成功！'
        return TR(request, 'WaitInfo.html',\
            {'urlx':urlx, 'display':display})
    return render(request, 'info.html', {'myself': myself[0],\
        'tip': tip, 'username': username},\
        context_instance=RequestContext(request))
        
def replays(req): 
    username=req.GET['userna']
    news_id=req.GET['news_id']
    if not 'username' in req.session:
        raise Http404
    user = User.objects.filter(username = username)
    if not user:
        raise Http404
    user = user[0] 
    content=req.GET['content']    
    if content:
		com_news=News.objects.filter(id=news_id)[0]      
		add_news=NewsComment(Newsinfo=com_news,user=user,content=content)#将评论写进数据库 
		add_news.save()
		#return  HttpResponse(json.dumps({"content":content}))
    replays = NewsComment.objects.filter(Newsinfo=com_news)#一条新闻的所有评
    url=com_news.source_url
    realurl='http://today.hit.edu.cn'+ url
    request = urllib2.Request(realurl)
    response = urllib2.urlopen(request)
    selector=etree.HTML(response.read().decode('gbk'))
    contents=selector.xpath("//div[@id='page_main']")
    info=contents[0].xpath('string(.)')   
    return render_to_response('新闻页test.html',{
		'replays':replays,
		'username':username,
		'view_news':com_news,
		'info':info,
		    },context_instance=RequestContext(req))