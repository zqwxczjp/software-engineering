#coding:utf-8
from django.db import models

# Create your models here.
class User(models.Model):
	'''主键使用默认id'''
	username = models.CharField(max_length = 50)	#用户名
	password = models.CharField(max_length = 50)	#密码，密码格式暂时不定
	email = models.EmailField()	#邮件，可用于验证，修改密码等
	institute = models.CharField(max_length = 50, null = True, blank = True)	#学院
	major = models.CharField(max_length = 50, null = True, blank = True)	#专业
	birthday = models.DateField(null = True, blank = True)	#生日
	icon = models.ImageField(upload_to = "./img", null = True, blank = True)	#用户头像
	degree = models.IntegerField(null = True, blank = True)	#等级
	state = models.IntegerField(blank = True, null = True)   #默认值为-1, 设置为1表示激活，用户正常
	active_code = models.CharField(max_length = 200, null = True, blank = True)
    
	def __unicode__(self):
		return self.username
class Friends(models.Model):
	userID = models.IntegerField()	#两者id较小的
	friendID = models.IntegerField()	#两者id较大的
    #-1:L->R; 1:R->L;0:L-R;
	ReqDirection = models.IntegerField(null = True, blank = True)
	def __unicode__(self):
		return '%d-%d' % (self.userID, self.friendID)

class ForwardNews(models.Model):
	'''转发消息'''
	user = models.ForeignKey(User)	#谁转发的
	url = models.URLField( null = True)
	title = models.CharField(max_length = 200, null = True, blank = True)
	time = models.TextField( null = True)
	def __unicode__(self):
		return self.url
#用户转发信息的评论表
class ForwardNewsComment(models.Model):
	'''转发消息的评论'''
	ForwardInfo = models.ForeignKey(ForwardNews)	#用户转发的消息的外键
	user = models.ForeignKey(User)	#谁评论的
	content = models.TextField()	#评论内容
	time = models.DateField(null = True, blank = True)	#评论时间
	def __unicode__(self):
		return self.content
class ReleaseMesg(models.Model):
	'''发布消息'''
	user = models.ForeignKey(User)
	content = models.TextField()
	time = models.DateField()
	def __unicode__(self):
		return self.content
class ReleaseMesgComment(models.Model):
	'''发布消息的评论'''
	ReleaseInfo = models.ForeignKey(ReleaseMesg)	#对哪个消息的评论
	user = models.ForeignKey(User)	#谁评论的
	content = models.TextField()	#内容
	time = models.DateField()	#时间
	def __unicode__(self):
		return self.content
class News(models.Model):
	'''从今日哈工大抓取的新闻'''
	source_url = models.URLField()	#源链接url
	title = models.TextField()	#新闻标题
	author = models.TextField()	#新闻作者
	content = models.TextField()	#新闻内容
	time = models.TextField()	#新闻发布时间
	recommend_index = models.TextField()	#推荐指数
	def __unicode__(self):
		return self.title
class InterestTribe(models.Model):
	'''兴趣部落，这个还需继续明确！！！应该没这么简单'''
	ThreadID = models.IntegerField()	#帖子id
	theme = models.CharField(max_length = 50)	#主题
	content = models.TextField()	
	user = models.ForeignKey(User)	
	def __unicode__(self):
		return self.theme

class NewsComment(models.Model):
	'''新闻的评论'''
	Newsinfo = models.ForeignKey(News)	#对哪个消息的评论
	user = models.ForeignKey(User)	#谁评论的
	content = models.TextField()	#内容
	time = models.DateField(null=True)	#时间
	def __unicode__(self):
		return self.content
        
class SendMesg(models.Model):
	'向好友发送私信'
	userFrom = models.IntegerField()
	userTo = models.IntegerField()
	Content = models.TextField()
	Time = models.DateTimeField(null = True, blank = True, auto_now_add = True)
	HasRead = models.BooleanField(default = False)
	def __unicode__(self):
		#str = '%s -> %s' % (self.userFrom.username, self.userTo.username)
		return self.Content
	