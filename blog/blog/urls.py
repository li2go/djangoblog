from django.conf.urls import patterns, include, url
from views import *
from django.contrib import admin
from djangoblog.api import ArticleResource
import settings
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',iindex),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/',include('account.urls')),
    url(r'^blog/',include('djangoblog.urls',namespace='blog')),
    
    url(r'^api/', include(ArticleResource().urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),    
    url(r'^ckeditor/', include('ckeditor.urls'))  ,
)
