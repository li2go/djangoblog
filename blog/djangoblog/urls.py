from djangoblog import views
from django.conf.urls import include,url,patterns
from djangoblog.api import ArticleResource

urlpatterns = patterns('',
	url(r'^$',views.index),
	#url(r'^Article', include(ArticleResource().urls)),

	)