#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Created by 安生 on 2017/2/26

from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.SnippetListView.as_view()),  # 获取snippet列表
    url(r'^(?P<pk>[0-9]+)/$', views.SnippetDetailView.as_view()),  # 差删改snippets
    url(r'^users/$', views.UserListView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
