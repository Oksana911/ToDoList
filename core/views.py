from rest_framework.generics import CreateAPIView
from core.models import User
from core.serializers import SignUpSerializer


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
