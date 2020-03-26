from django.conf.urls import url, include
from django.contrib import admin
from captcha.views import captcha_refresh

from django.conf import settings
from django.conf.urls.static import static

from .custom_site import custom_site
from blog.views import *
from config.views import LinkListView
from comment.views import CommentView
from django.contrib.sitemaps import views as sitemap_views
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap

from registration.backends.hmac.views import RegistrationView
from logininfo.forms import CustomRegsterForm

from autocomplete import CategoryAutocomplete, TagAutocomplete

from logininfo import urls as lu
from logininfo import views as lv

from pollitem import urls as pu

from mainsite import urls as mu

urlpatterns = [
    # 博客
    url(r"^$", IndexView.as_view(), name="index"),
    url(r"^category/(?P<category_id>\d+)/$", CategoryView.as_view(), name="category-list"),
    url(r"^tag/(?P<tag_id>\d+)/$", TagView.as_view(), name="tag-list"),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name="post-detail"),
    url(r'^links/$', LinkListView.as_view(), name="links"),
    url(r"^search/$", SearchView.as_view(), name="search"),
    url(r"^author/(?P<owner_id>\d+)/$", AuthorView.as_view(), name="author"),

    # 网站地图
    url(r'^rss|feed/', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps':{'posts': PostSitemap}}),

    # 日记路由
    url(r"^diary/", include(lu)),
    url(r'^login/$', lv.login),
    url(r'^logout/$', lv.logout),
    url(r'^userinfo/$', lv.userinfo),
    url(r'^ver/$', lv.userver, name='ver'),

    # 商城路由
    url(r"^myshop/", include(pu)),

    # 投票路由
    url(r'mvote/', include(mu)),

    url(r'^accounts/register/$',
        RegistrationView.as_view(
            form_class=CustomRegsterForm
        ),
        name='registration_register',
    ),

    # autocomplete配置
    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),

    url(r'^super_admin/', admin.site.urls, name="admin"),
    url('^refresh/',captcha_refresh),
    url(r'mdeditor/', include('mdeditor.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^filer/$', include('filer.urls')),
    url(r'^captcha/', include('captcha.urls')),
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^admin/', custom_site.urls, name='admin'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

