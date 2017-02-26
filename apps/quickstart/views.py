from django.shortcuts import render
from django.contrib.auth.models import User, Group
from quickstart.serializers import UserSerializers, GroupSerializers
from rest_framework import viewsets


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    查看、编辑用户的界面
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
    """
    查看、编辑组的界面
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
