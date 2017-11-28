from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    # or you can make it views.home, name = "home" and make corresponding change in views.py
    url(r'^$', views.homepage), 
    url(r'^login/$', login, {"template_name":"accounts/login.html"}, name = 'login'),   
    url(r'^logout/$', logout, {"template_name":"accounts/logout.html"}, name = 'logout'),   
    url(r'^register/$', views.register,  name="register"),   
    url(r'^profile/$', views.view_profile,  name="view_profile"),   
    url(r'^profile/edit/$', views.edit_profile,  name="edit_profile"),   

    url(r'^change-password/$', views.change_password, name = "change_password"),
    url(r'^reset-password/$', password_reset, name = "reset_password"),
    url(r'^reset-password/done$', password_reset_done, name = "password_reset_done"),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    password_reset_confirm, name = "password_reset_confirm"),
    url(r'^reset-password/complete/$', password_reset_complete, name = "password_reset_complete"),

     url(r'^clubinfo/$', views.clubinfo, name='clubinfo'), 
     url(r'^courseinfo/$', views.courseinfo, name='courseinfo'), 
     url(r'^freeride/$', views.freeride, name='freeride'), 
     url(r'^privatetutor/$', views.privatetutor, name='privatetutor'), 
     url(r'^rentinfo/$', views.rentinfo, name='rentinfo'),

      url(r'^add_post.html/$', views.add_post, name='add_post'),
     url(r'^post_list.html$', views.post_list, name='post_list'),
     url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
     url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

]
#python3 -m smtpd -n -c DebuggingServer localhost:1025