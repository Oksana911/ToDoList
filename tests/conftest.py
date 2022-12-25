import pytest
from rest_framework.test import APIClient
from core.models import User
from goals.models import GoalCategory, Board, BoardParticipant


# from factories import UserFactory, CategoryFactory, BoardFactory, BoardParticipantFactory


@pytest.fixture
def auth_user(test_user):
    user = APIClient()
    user.force_authenticate(test_user)
    return user


@pytest.fixture
def test_user(db):
    user = User.objects.create(username='Petr', password='1234qwe4321', email='petr@petr.ru')
    return user


@pytest.fixture
def category(board, test_user):
    return GoalCategory.objects.create(user=test_user, board=board)


@pytest.fixture
def board():
    return Board.objects.create()


@pytest.fixture
def board_part(test_user, board):
    return BoardParticipant.objects.create(
        user=test_user,
        board=board,
    )
