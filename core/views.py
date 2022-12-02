from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import User
from core.serializers import SignUpSerializer, LoginSerializer


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class LoginView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request=request,
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        if user is None:
            raise AuthenticationFailed
        else:
            login(request, user)
            return Response(serializer.data), status.HTTP_201_CREATED


# @ensure_csrf_cookie
# class ProfileView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated|ReadOnly]


