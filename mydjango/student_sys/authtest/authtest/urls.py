from django.conf.urls import include, url
from django.contrib import admin

from usertest import views as uv

urlpatterns = [
    # Examples:
    # url(r'^$', 'authtest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', uv.index),
    url(r'^login/', uv.login),
    url(r'^userinfo/', uv.useinfo),
    url(r'^post/', uv.posting),
    url(r'^logout/', uv.logout),
    url(r'^admin/', include(admin.site.urls)),
]
