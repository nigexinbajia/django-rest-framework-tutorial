#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Created by 安生 on 2017/2/26

from django.contrib.auth.models import User, Group
from rest_framework import serializers

"""
使用HyperlinkedModelSerializer来建立超链接关系
"""


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
