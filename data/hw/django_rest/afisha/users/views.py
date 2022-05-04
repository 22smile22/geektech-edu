#from django.shortcuts import render
# Create your views here.

#hw5
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UserValidateSerializers, UserAuthorizationSerializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView  #hw6


#hw6
class RegisterAPIView(APIView):
    serializer_class = UserValidateSerializers
    model_class = User

    def post(self, request, *args, **kwargs):
        # serializer = UserValidateSerializers(data=request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # User.objects.create_user(**serializer.validated_data)
        self.model_class.create_user(**serializer.validated_data)
        return Response(data={'message': 'User created'})


# @api_view(['POST'])
# def registration(request):
#     serializer = UserValidateSerializers(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     # username = request.data.get('username') # admin
#     # password = request.data.get('password') # 1234
#     # User.objects.create_user(password=password, username=username)
#     User.objects.create_user(**serializer.validated_data)
#     return Response(data={'message': 'User created'})


class AuthAPIView(APIView):
    def post(self, request):
        serializer = UserAuthorizationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'key': token.key})
        return Response(data={'message': 'User not found'},
                        status=404)


# @api_view(['POST'])
# def authorization(request):
#     serializer = UserAuthorizationSerializers(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(username=username, password=password)
#     if user:
#         try:
#             token = Token.objects.get(user=user)
#         except Token.DoesNotExist:
#             token = Token.objects.create(user=user)
#         return Response(data={'key': token.key})
#     return Response(data={'message': 'User not found'},
#                     status=404)
