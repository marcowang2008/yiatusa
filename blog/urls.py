from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    # ex: /blog/
    url(r'^$', views.index, name='index'),
#    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /blog/5/
    url(r'^(?P<post_id>\d+)/$', views.post, name='post'), 
#    url(r'^(?P<pk>\d+)/$', views.PostView.as_view(), name='post'),  
    # ex: /blog/5/addComment/
    url(r'^(?P<post_id>\d+)/add_comment/$', views.add_comment, name='addComment'),#ToDo: change this to ajax!!!
    # /blog/category/1/
    url(r'^category/(?P<cate_id>\d+)/$', views.category, name='category'),
    # /blog/tag/1
    url(r'^tag/(?P<t_id>\d+)/$', views.tag, name='tag'),
    
    
)

