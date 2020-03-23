from django.conf.urls import include, url
from django.contrib import admin

from mainsite import views as mv



urlpatterns = [
    # Examples:
    # url(r'^$', 'mvote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', mv.index),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^poll/(\d+)$', mv.poll, name='poll-url'),
    url(r'^vote/(\d+)/(\d+)$', mv.vote, name='vote.url'),
    url(r'^admin/', include(admin.site.urls)),
]
