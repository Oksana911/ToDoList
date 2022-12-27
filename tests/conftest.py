import pytest
from rest_framework.test import APIClient
from factories import CategoryFactory, BoardFactory, BoardParticipantFactory, GoalFactory, CommentFactory


@pytest.fixture
def test_user(db, django_user_model):
    user = django_user_model.objects.create_user(username='Petr', password='1234qwe4321', email='petr@petr.ru')
    return user


@pytest.fixture
def auth_user(test_user):
    user = APIClient()
    user.force_authenticate(test_user)
    return user


@pytest.fixture
def board():
    return BoardFactory.create()


@pytest.fixture
def board_part(test_user, board):
    return BoardParticipantFactory.create(
        user=test_user,
        board=board,
    )


@pytest.fixture
def category(test_user, board, board_part):
    return CategoryFactory.create(user=test_user, board=board)


@pytest.fixture
def goal(category, test_user):
    return GoalFactory.create(category=category, user=test_user)


@pytest.fixture
def comment(goal, test_user):
    return CommentFactory.create(goal=goal, user=test_user)
