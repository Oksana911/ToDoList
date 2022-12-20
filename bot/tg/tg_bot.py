from bot.models import TgUser
from client import TgClient


class TgBot:
    def __init__(self, tg_client: TgClient):
        self.tg_client = tg_client

    def check_user(self, tg_user_id: int, tg_chat_id: int):
        """Проверка наличия пользователя в БД"""
        user, created = TgUser.objects.get_or_create(tg_user_id, tg_chat_id)

        if created:
            user.save()
            self.tg_client.send_message(chat_id=tg_chat_id, text='Привет!')
            return user
        else:
            self.tg_client.send_message(chat_id=tg_chat_id, text='Ты уже был!')
            return user
