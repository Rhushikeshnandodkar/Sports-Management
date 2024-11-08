from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import UserInfoSerializer
from rest_framework import status
# Create your views here.

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            serializer_data = {
                'refresh':str(refresh),
                'access':str(refresh.access_token),
                'user':serializer.data
            }
            return Response(serializer_data)
        return Response(serializer.errors)
    
class UserInfoApiView(APIView):
    serializer_class = UserInfoSerializer
    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserInfoSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {"message":"user is not authenticated"}
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)
    def patch(self, request, format=None):
        if request.user.is_authenticated:
            model = CustomUser.objects.get(id=request.user.id)
            serializer = UserInfoSerializer(model, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                messsage = {"message": "Phone number allready exists"}
                return Response(messsage, status=status.HTTP_409_CONFLICT)
        messsage = {"message": "please login"}
        return Response(messsage, status=status.HTTP_401_UNAUTHORIZED)