from .models import UserPost
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = '__all__' #모두 적용시킬 경우
        #fields = ('id', 'title', 'body')
        #read_only_fields = ('title',)