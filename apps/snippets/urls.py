#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Created by 安生 on 2017/2/26

from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.snippet_list),  # 获取snippet列表
    url(r'^(?P<pk>[0-9]+)/$', views.snippet_detail),  # 差删改snippets
]

urlpatterns = format_suffix_patterns(urlpatterns)
