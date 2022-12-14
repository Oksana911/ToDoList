# Generated by Django 4.0.1 on 2022-12-21 07:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_rename_telegram_chat_id_tguser_tg_chat_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='tg_username',
            field=models.CharField(default='', max_length=32, validators=[django.core.validators.MinLengthValidator(5)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tguser',
            name='verification_code',
            field=models.CharField(default='', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
