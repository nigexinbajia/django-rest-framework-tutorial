#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Created by 安生 on 2017/2/26

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)  # 只读
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)  # 不能为空
    code = serializers.CharField(style={'base_template': 'textarea.html'})  # 代码
    linenos = serializers.BooleanField(required=False)  # 不能为空
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')  # 语言
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')  # 渲染的样式

    def create(self, validated_data):
        """
        如果数据合法就创建并返回一个snippet实例
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        如果数据合法就更新并返回一个存在的snippet实例
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
