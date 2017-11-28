from django.contrib import admin
from InfoTrack.models import UserProfile, Comment,Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #inlines = [CommentInline]
    list_display = ("title",'context', 'time')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    #inlines = [CommentInline]
    list_display = ('context', 'time')

"""
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username','time',"userid")

"""
admin.site.register(UserProfile)


