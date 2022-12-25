import factory
from goals.models import GoalCategory, User, Board, BoardParticipant, Goal, GoalComment


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = 'CommonPassword54321'
    email = factory.Faker('email')


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = factory.Faker('name')


class BoardParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BoardParticipant


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalCategory

    title = factory.Faker('name')


class GoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Goal

    title = factory.Faker('name')


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalComment

    text = factory.Faker('name')
