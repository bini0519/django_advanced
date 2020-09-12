from post.models import Post
from post.serializer import PostSerializer

from rest_framework import generics
from rest_framework import mixins

class PostList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    #등록(generics.GenericAPIView 안에서 선언된 변수임)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    #필요로 하는 메서드
    #가변인자 사용(인자의 개수에 상관없이 받음)
    def get(self, request, *args, **kwargs):
        #list는 ListModelMixin에서 이미 정의된 메서드
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        #create는 CreateModelMixin에서 이미 정의된 메서드
        return self.create(request, *args, **kwargs)

class PostDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)