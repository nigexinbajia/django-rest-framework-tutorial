#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Created by 安生 on 2017/2/26
from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# API endpoints
urlpatterns = [
    url(r'^', include(router.urls)),
]