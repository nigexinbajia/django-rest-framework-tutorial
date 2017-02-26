#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Created by 安生 on 2017/2/26

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    自定义权限，只有创建者才能编辑
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user
