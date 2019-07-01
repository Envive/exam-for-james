from rest_framework import serializers
from .models import Post, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

        # for PUT
        extra_kwargs = {
            'user_id': {'required': False},
            'title': {'required': False},
            'content': {'required': False}
        }

    # def update(self, instance, validated_data):
    #
    #     instance.user_id = validated_data.get('user_id', instance.user_id)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #
    #     return instance
