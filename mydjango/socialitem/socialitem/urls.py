from django.conf.urls import include, url
from django.contrib import admin

from pollitem import views as pv

urlpatterns = [
    # Examples:
    # url(r'^$', 'socialitem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^poll/(\d+)$', pv.poll, name='poll-url'),
    url(r'^govote/$', pv.govote),
    url(r'^addpoll/$', pv.addpoll, name='addpoll-url'),
    url(r'^updatepollitem/(\d+)$', pv.updatepollitem, name='addpollitem-url'),
    url(r'^vote/(\d+)/(\d+)$', pv.vote, name='vote-url'),
    url(r'^$', pv.index, name='index'),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
