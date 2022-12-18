from django.core.management.base import BaseCommand
from bot.tg.client import TgClient


class Command(BaseCommand):
    def handle(self, *args, **options):
        offset = 0
        tg_client = TgClient("5964107256:AAEiTpzP8gyyE1RTrfJL6TJcduFgpz1Y7i4")
        while True:
            res = tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
                print(item.message)
