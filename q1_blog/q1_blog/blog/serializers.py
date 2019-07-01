from rest_framework import serializers
from .models import Post, User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'created_at')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user_id', 'title', 'content', 'created_at', 'updated_at')
