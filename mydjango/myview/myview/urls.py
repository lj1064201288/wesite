from django.conf.urls import include, url
from django.contrib import admin
from view_learing import view_learing_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'myview.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^viewlear/', include(view_learing_urls)),

]
