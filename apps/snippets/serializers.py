#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Created by 安生 on 2017/2/26

from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User

"""
HyperlinkedModelSerializer默认不包含主键
HyperlinkedModelSerializer自动包含URL字段HyperlinkedIdentityField
使用HyperlinkedRelatedField来替代PrimaryKeyRelatedField表示关系
"""


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # 只读类型，用于进行序列化时候的展示，并且反序列化时不会被修改。
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('id', 'highlight', 'owner', 'created', 'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
