# Generated by Django 4.0.1 on 2022-12-19 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tguser',
            old_name='telegram_chat_id',
            new_name='tg_chat_id',
        ),
        migrations.RenameField(
            model_name='tguser',
            old_name='telegram_user_ud',
            new_name='tg_user_id',
        ),
    ]
