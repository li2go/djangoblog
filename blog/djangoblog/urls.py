from djangoblog import views
from django.conf.urls import include,url,patterns

urlpatterns = patterns('',
	url(r'^$',views.index),

	)