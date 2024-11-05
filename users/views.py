from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
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
