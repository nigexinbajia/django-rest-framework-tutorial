#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Created by 安生 on 2017/2/26
from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# API endpoints
urlpatterns = [
    url(r'^', include(router.urls)),
]
