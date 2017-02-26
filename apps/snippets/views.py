from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# Create your views here.

class JSONResponse(HttpResponse):
    """
    用于返回JSON数据
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)  # 序列化
        kwargs['content_type'] = 'application/json'  # 返回类型
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def snippet_list(request):
    """
    展示所有snippets，或创建新的snippet
    """
    if request.method == 'GET':
        """
        如果是GET请求就获取所有代码段，并通过JSONResponse返回给前端
        """
        snippets = Snippet.objects.all()
        serializers = SnippetSerializer(snippets, many=True)  # 显示多条
        return JSONResponse(serializers.data)
    elif request.method == 'POST':
        """
        如果是POST，获取请求头里面的数据，交给serializers验证，如果格式验证成功就保存并发数据返回到前端，否则返回格式错误的信息给前端
        """
        data = JSONParser().parse(request)
        serializers = SnippetSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return JSONResponse(serializers.data, status=201)
        return JSONResponse(serializers.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    修改或删除一个snippet
    """
    try:
        """
        获取snippet数据，如果获取不到就返回404
        """
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        """
        如果是GET方法，通过SnippetSerializer获取到代码片段并以JSON数据返回给前端
        """
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        """
        如果是POST请求，则获取请求头里面的数据，然后交给SnippetSerializer进行验证， 如果格式正确就更新，否则就返回错误信息
        """
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        """
        如果是DELETE则直接删除代码段
        """
        snippet.delete()
        return HttpResponse(status=204)
