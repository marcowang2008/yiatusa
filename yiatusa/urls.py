from django.conf.urls import patterns, include, url
from home import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yiatusa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    # home app is used to serve 'static' page with template
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    # admin app
    url(r'^admin/', include(admin.site.urls)),
    # blog app
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^tinymce/', include('tinymce.urls')),
#    url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    
)
