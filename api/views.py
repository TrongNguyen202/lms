# authentication_app/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CustomUser, Course
from .serializers import CustomUserSerializer, CourseSerializer
from django.core.mail import send_mail
from django.conf import settings

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Generate and send verification code
            verification_code = "123456"  # You can use a library to generate a random code
            user.verification_code = verification_code
            user.save()

            send_mail(
                'Verification Code',
                f'Your verification code is: {verification_code}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            return Response({'detail': 'User registered successfully. Check your email for the verification code.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



