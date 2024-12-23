from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    # Your other routes...
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register-user', RegisterAPIView.as_view()),
    path('user-info', UserInfoApiView.as_view(), name="user-info"),
    path('get-students', StudentProfileApiView.as_view()),
    path('create-profile', CreateStudentProfileApiView.as_view())


]