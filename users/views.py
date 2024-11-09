from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import UserInfoSerializer
from rest_framework import status
from .permissions import *
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
    
class StudentProfileApiView(APIView):
    serializer_class = StudentProfileSerializer
    def get(self, request):
        user = request.user
        if user.is_authenticated and (user.user_type == 'admin' or user.user_type == 'coordinator'):
            model = StudentProfile.objects.all()
            serializer = StudentProfileSerializer(model, many=True)
            return Response(serializer.data)
        message = {"message" : "you don't have authority to see data"}
        return Response(message, status=status.HTTP_401_UNAUTHORIZED)
    
class CreateStudentProfileApiView(APIView):
    permission_classes = [IsAuthenticatedUser]
    serializer_class = StudentProfileSerializer
    def post(self, request, format=None):
        if StudentProfile.objects.filter(user=request.user).exists():
            return Response({"message" : "Profile allready exists"}, status=status.HTTP_400_BAD_REQUEST)
        data = request.data.copy()
        data['user'] = request.user.id 
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, format=None):
        if request.user.is_authenticated:
            try:
                profile = StudentProfile.objects.get(user=request.user.id)
            except StudentProfile.objects.get(user=request.user.id).DoesNotExist:
                return Response({"message" : "Profile does not exists"}, status=status.HTTP_404_NOT_FOUND)
            serializer = StudentProfileSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
        message = {"message" : "you don't have authority to see data"}
        return Response(message, status=status.HTTP_401_UNAUTHORIZED)