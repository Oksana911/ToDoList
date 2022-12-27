import pytest
from rest_framework.test import APIClient
from core.models import User
from factories import CategoryFactory, BoardFactory, BoardParticipantFactory, GoalFactory, CommentFactory
from goals.models import Board, BoardParticipant, GoalCategory, Goal


@pytest.fixture
def test_user(db, django_user_model) -> User:
    user = django_user_model.objects.create_user(username='Petr', password='1234qwe4321', email='petr@petr.ru')
    return user


@pytest.fixture
def auth_user(test_user: User) -> APIClient:
    user = APIClient()
    user.force_authenticate(test_user)
    return user


@pytest.fixture
def board():
    return BoardFactory.create()


@pytest.fixture
def board_part(test_user: User, board: Board):
    return BoardParticipantFactory.create(
        user=test_user,
        board=board,
    )


@pytest.fixture
def category(test_user: User, board: Board, board_part: BoardParticipant):
    return CategoryFactory.create(user=test_user, board=board)


@pytest.fixture
def goal(category: GoalCategory, test_user: User):
    return GoalFactory.create(category=category, user=test_user)


@pytest.fixture
def comment(goal: Goal, test_user: User):
    return CommentFactory.create(goal=goal, user=test_user)
