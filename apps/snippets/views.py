from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView


# Create your views here.

class SnippetListView(ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetailView(RetrieveDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
