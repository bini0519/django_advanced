from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' #모두 적용시킬 경우
        #fields = ('id', 'title', 'body')
        #read_only_fields = ('title',)