from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListCreateAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly  # 类确保了只有认证用户才有读写权限，未认证用户则只有只读权限。
from snippets.permissions import IsOwnerOrReadOnly


# Create your views here.

class SnippetListView(ListCreateAPIView):  # GET/POST
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetailView(RetrieveUpdateDestroyAPIView):  # GET/PUT/PATCH/DELETE
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class UserListView(ListAPIView):  # GET
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):  # GET
    queryset = User.objects.all()
    serializer_class = UserSerializer
