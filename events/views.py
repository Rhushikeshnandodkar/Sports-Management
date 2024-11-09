from django.shortcuts import render
from rest_framework.generics import *
from .serializers import *
from rest_framework.permissions import AllowAny
# Create your views here.
class EventsListApiView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = EventSerializer
    queryset = EventModel.objects.all()