from account import views
from django.conf.urls import include,url,patterns

urlpatterns = patterns('',
	url(r'^register/$',views.register,name='register'),

	)