from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	email = models.EmailField()
	institute = models.CharField(max_length = 50)
	major = models.CharField(max_length = 50)
	birthday = models.DateField()
	icon = models.ImageField(upload_to = "./img")
	degree = models.IntegerField()

class Friends(models.Model):
	userID = models.IntegerField()
	friendID = models.IntegerField()	

class UserForwardInfo(models.Model):
	user = models.ForeignKey(User)
	url = models.URLField()
	time = models.DateField()
	comments = models.TextField()	#set??

class UserReleaseInfo(models.Model):
	user = models.ForeignKey(User)
	content = models.TextField()
	time = models.DateField()
	comments = models.TextField()	#set??

class News(models.Model):
	source_url = models.URLField()
	title = models.TextField()
	author = models.TextField()
	content = models.TextField()
	time = models.TextField()
	recommend_index = models.IntegerField()

class InterestTribe(models.Model):
	ThreadID = models.IntegerField()
	theam = models.CharField(max_length = 50)
	content = models.TextField()
	user = models.ForeignKey(User)

