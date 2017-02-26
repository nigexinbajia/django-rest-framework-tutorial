from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class SnippetListView(APIView):
    """
    展示或创建snippets.
    """

    def get(self, request, format=None):
        """
        如果是GET请求就获取所有代码段，并通过JSONResponse返回给前端
        """
        snippets = Snippet.objects.all()
        serializers = SnippetSerializer(snippets, many=True)  # 显示多条
        return Response(serializers.data)

    def post(self, request, format=None):
        """
        如果是POST，获取请求头里面的数据，交给serializers验证，如果格式验证成功就保存并发数据返回到前端，否则返回格式错误的信息给前端
        """
        serializers = SnippetSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetailView(APIView):
    """
    修改或删除一个snippet
    """

    def get_object(self, pk):
        try:
            """
            获取snippet数据，如果获取不到就返回404
            """
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        """
       如果是GET方法，通过SnippetSerializer获取到代码片段并以JSON数据返回给前端
       """
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        如果是PUT请求，则获取请求头里面的数据，然后交给SnippetSerializer进行验证， 如果格式正确就更新，否则就返回错误信息
        """
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        """
        如果是DELETE则直接删除代码段
        """
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=204)
