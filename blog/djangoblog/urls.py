from djangoblog import views
from django.conf.urls import include,url,patterns
from djangoblog.api import ArticleResource
#from django.conf import settings if settings.DEBUG is False:

urlpatterns = patterns('',
	url(r'^$',views.index,name='home'),
	url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(), name='detail'),
	 )