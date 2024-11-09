from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
      path('events-list', EventsListApiView.as_view(), name="events-info"),


]