from django.conf.urls import include, url
from django.contrib import admin
from test_objects.views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'test_ms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
]
