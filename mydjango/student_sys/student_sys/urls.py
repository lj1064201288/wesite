from django.conf.urls import include, url
from django.contrib import admin
from student.views import IndexView

urlpatterns = [
    # Examples:
    # url(r'^$', 'student_sys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
