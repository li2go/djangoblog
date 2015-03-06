from django.conf.urls import patterns, include, url
from djangoblog.views import index
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/',include('account.urls')),
    url(r'^$',include('djangoblog.urls'))
)
