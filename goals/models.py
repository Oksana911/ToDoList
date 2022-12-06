from django.db import models
from core.models import User


# aбстрактный класс, описывающий поля created и updated
# остальные модели сущностей наследуются от него
class DatesModelMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')


class GoalCategory(DatesModelMixin):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(verbose_name='Название', max_length=255)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT)
    is_deleted = models.BooleanField(verbose_name='Удалена', default=False)


######################################

class Status(models.IntegerChoices):
    to_do = 1, 'К выполнению'
    in_progress = 2, 'В процессе'
    done = 3, 'Выполнено'
    archived = 4, 'Архив'


class Priority(models.IntegerChoices):
    low = 1, 'Низкий'
    medium = 2, 'Средний'
    high = 3, 'Высокий'
    critical = 4, 'Критический'


class Goal(DatesModelMixin):
    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    category = models.ForeignKey(GoalCategory, verbose_name='Категория', on_delete=models.CASCADE,
                                 related_name='goals')
    due_date = models.DateTimeField(verbose_name='Дедлайн', blank=True, null=True)
    status = models.PositiveSmallIntegerField(
        verbose_name='Статус', choices=Status.choices, default=Status.to_do
    )
    priority = models.PositiveSmallIntegerField(
        verbose_name='Приоритет', choices=Priority.choices, default=Priority.medium
    )


##########################################


class GoalComment(DatesModelMixin):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    text = models.CharField(verbose_name='Комментарий', max_length=400)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, verbose_name='Цель', on_delete=models.CASCADE)
