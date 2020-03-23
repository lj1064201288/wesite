"""ch09www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from formtest import views as fv

urlpatterns = [
    url(r'^$', fv.index),
    url(r'^contact/$', fv.contact),
    url(r'^list/$', fv.listing),
    url(r'^login/$', fv.login),
    url(r'^logout/$', fv.logout),
    url(r'^userinfo/$', fv.userinfo),
    url(r'^post/$', fv.posting),
    url(r'^post2db/$', fv.post2db),
    url(r'^(\d+)/(\w+)$', fv.index),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
