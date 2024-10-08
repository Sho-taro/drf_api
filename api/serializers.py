from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
            }
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # パスワードをハッシュ化して保存
        Token.objects.create(user=user)  # トークンの生成？
        return user


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'created_at', 'updated_at']