from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins ,generics
from account.serializers import *
from django.contrib.auth import authenticate
from account.renderer import UserRenderer
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



# Create your views here.

class RegisterApi(APIView):
    renderer_classes = [UserRenderer]
    def get(self,request):
        user = User.objects.all()
        serializers = UserSerializer(user , many = True)
        return Response(serializers.data)
    def post(self,request,formate = None):
        data = request.data 
        serializers = UserSerializer(data = data)
        if serializers.is_valid(raise_exception=True):
            user = serializers.save()
            token = get_tokens_for_user(user)
            return Response({"token":token, "msg":"registration success"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserLoginApi(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email= email, password = password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({"token":token,"msg": "login success"} ,status= status.HTTP_200_OK)
            else:
                return Response({"errors":{"non_field_errors":["password or email is not valid"]}}, status= status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
            


class ProfileAPi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
        

class ChangePassword(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer  = ChangePasswordSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = request.user 
            print(user)

            # Access validated data instead of `serializer.data`
            password = serializer.validated_data.get("password")
            confirm_password = serializer.validated_data.get("confirm_password")
            print(password, confirm_password)
            
            # Here you could also proceed with changing the password logic
            user.set_password(password)
            user.save() 
            
            return Response({"message": "Password changed successfully"})
        else:
            return Response(serializers.errors)

class SendPasswordResetEmailView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)
  

class UserPasswordResetView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
  



