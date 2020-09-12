from post.models import Post
from post.serializer import PostSerializer
from rest_framework import viewsets
from post.pagination import MyPagination

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    pagination_class = MyPagination