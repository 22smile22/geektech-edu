#hw5
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class UserValidateSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise ValidationError('User already exists!!!')
        return username

class UserAuthorizationSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
