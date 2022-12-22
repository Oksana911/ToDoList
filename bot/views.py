from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from bot.models import TgUser
from bot.serializers import TgUserSerializer
from bot.tg.client import TgClient


class BotView(UpdateAPIView):
    model = TgUser
    serializer_class = TgUserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']

    def patch(self, request, *args, **kwargs):
        data = self.serializer_class(request.data).data

        tg_client = TgClient("5964107256:AAEiTpzP8gyyE1RTrfJL6TJcduFgpz1Y7i4")
        tg_user = TgUser.objects.filter(verification_code=data['verification_code']).first()

        if not tg_user:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        tg_user.user = request.user
        tg_user.save()
        tg_client.send_message(chat_id=tg_user.tg_chat_id, text='Бот успешно привязан')
        return Response(data=data, status=status.HTTP_200_OK)
