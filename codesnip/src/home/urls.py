from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.redirecthome, name='home'),
    url(r'^home/$', views.redirecthome, name='home'),
    url(r'^home/snippets/$', views.home, name='home'),
	url(r'^submit/$', views.submit, name='submit'),
    url(r'^submit/add_snippets/$', views.add_snippet, name='add_snippet'),
    url(r'^home/snippets/(?P<id>\d+)/$', views.view_snippet, name='view_snippet'),
    url(r'^home/snippets/(?P<id>\d+)/edit_snippet/$', views.edit_snippet, name='edit_snippet'),
    url(r'^home/snippets/(?P<id>\d+)/delete_snippet/$', views.delete_snippet, name='delete_snippet'),
    url(r'^home/snippets/(?P<id>\d+)/upvote_snippet/$', views.upvote_snippet, name='upvote_snippet'),
    url(r'^home/snippets/(?P<id>\d+)/downvote_snippet/$', views.downvote_snippet, name='downvote_snippet'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]