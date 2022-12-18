from django.db import models
from core.models import User


class TgUser(models.Model):
    telegram_chat_id = models.IntegerField()
    telegram_user_ud = models.IntegerField()
    user = models.ForeignKey(User, null=True, blank=True)
