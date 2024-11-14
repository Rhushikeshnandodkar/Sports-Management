from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import *
from events.models import *
from rest_framework.permissions import AllowAny
from rest_framework import status
from users import permissions
from .serializers import IndApplicationSerializer
from .models import *
# Create your views here.
class IndApplicationApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedUser]
    serializer_class = IndApplicationSerializer
    def post(self, request, event_id):
        event = IndApplicationModel.objects.get(event=event_id)
        try:
            profile = StudentProfile.objects.get(user=request.user)
        except StudentProfile.DoesNotExist:
            return Response({"error": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)

        application = IndApplicationModel.objects.create(
            event=event,
            profile = profile,
            stage = 'Applied',
            note = request.data.get("note", ''),
            reviewed_by=request.data.get("reviewed_by", "") 
        )
        serializer = IndApplicationSerializer(application)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
