from post.models import Post
from post.serializer import PostSerializer

from rest_framework import viewsets

from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse

'''
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #필요로 하는 메서드
    #가변인자 사용(인자의 개수에 상관없이 받음)
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        #직접 Response()를 리턴한다.
        return HttpResponse("성공")