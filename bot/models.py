from django.core.validators import MinLengthValidator
from django.db import models
from core.models import User
from django.utils.crypto import get_random_string


class TgUser(models.Model):
    tg_chat_id = models.IntegerField()
    tg_user_id = models.IntegerField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)])
    verification_code = models.CharField(max_length=10, unique=True)

    def generate_verification_code(self) -> str:
        ver_code = get_random_string(10)
        self.verification_code = ver_code
        self.save()
        return ver_code

