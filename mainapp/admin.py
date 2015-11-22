from django.contrib import admin
from mainapp.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password','email','institute', 'major')

class FriendsAdmin(admin.ModelAdmin):
    list_display = ('userID', 'friendID')

class ForwardMesgAdmin(admin.ModelAdmin):
	list_display = ('url', 'time')

class ForwardMesgCommentAdmin(admin.ModelAdmin):
	list_display = ('content', 'time')

class ReleaseMesgAdmin(admin.ModelAdmin):
	list_display = ('content', 'time')

class ReleaseMesgCommentAdmin(admin.ModelAdmin):
	list_display = ('content', 'time')

class NewsAdmin(admin.ModelAdmin):
	list_display = ('source_url', 'title', 'author')

class InterestTribeAdmin(admin.ModelAdmin):
	list_display = ('ThreadID', 'theme')

admin.site.register(User, UserAdmin)
admin.site.register(Friends, FriendsAdmin)
admin.site.register(ForwardMesg, ForwardMesgAdmin)
admin.site.register(ForwardMesgComment, ForwardMesgCommentAdmin)
admin.site.register(ReleaseMesg, ReleaseMesgAdmin)
admin.site.register(ReleaseMesgComment, ReleaseMesgCommentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(InterestTribe, InterestTribeAdmin)