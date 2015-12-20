from django.contrib import admin
from mainapp.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','id', 'password','email','institute', 'major')

class FriendsAdmin(admin.ModelAdmin):
    list_display = ('userID', 'friendID', 'ReqDirection')

class ForwardNewsAdmin(admin.ModelAdmin):
	list_display = ('url', 'time')

class ForwardNewsCommentAdmin(admin.ModelAdmin):
	list_display = ('content', 'time')

class ReleaseMesgAdmin(admin.ModelAdmin):
	list_display = ('content', 'time')

class ReleaseMesgCommentAdmin(admin.ModelAdmin):
	list_display = ('content', 'time')

class NewsAdmin(admin.ModelAdmin):
	list_display = ('source_url', 'title', 'author')

class InterestTribeAdmin(admin.ModelAdmin):
	list_display = ('ThreadID', 'theme')

class SendMesgAdmin(admin.ModelAdmin):
	list_display = ('userFrom', 'userTo', 'Time')
	
admin.site.register(User, UserAdmin)
admin.site.register(Friends, FriendsAdmin)
admin.site.register(ForwardNews, ForwardNewsAdmin)
admin.site.register(ForwardNewsComment, ForwardNewsCommentAdmin)
admin.site.register(ReleaseMesg, ReleaseMesgAdmin)
admin.site.register(ReleaseMesgComment, ReleaseMesgCommentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(InterestTribe, InterestTribeAdmin)
admin.site.register(SendMesg, SendMesgAdmin)