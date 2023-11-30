from django.urls import path
from .views import register_user, CourseList
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
                 path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
                  path('register/', register_user, name='register_user'),
                  path('courses/', CourseList.as_view(), name='course-list'),
                 
                  ]
