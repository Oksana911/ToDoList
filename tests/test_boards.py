import json
import pytest
from django.urls import reverse
from core.models import User
from factories import BoardParticipantFactory
from goals.models import Board, BoardParticipant
from goals.serializers.board import BoardSerializer, BoardListSerializer
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create(auth_user: APIClient, test_user: User):
    url = reverse('board_create')

    payload = {'title': 'new board'}
    response = auth_user.post(
        path=url,
        data=payload
    )
    response_data = response.json()

    assert response.status_code == 201
    assert response_data['title'] == payload['title']


@pytest.mark.django_db
def test_get_one(auth_user: APIClient, test_user: User, board: Board, board_part: BoardParticipant):
    url = reverse('board', kwargs={'pk': board.pk})
    response = auth_user.get(path=url)
    response_data = response.json()

    expected_response = BoardSerializer(board).data

    assert response.status_code == 200
    assert response_data == expected_response


@pytest.mark.django_db
def test_get_list(auth_user: APIClient, test_user: User, board: Board):
    participant = BoardParticipantFactory.create(board=board, user=test_user)

    response = auth_user.get(f"{reverse('boards_list')}?limit=1")
    expected_response = {
        'count': 1,
        'next': None,
        'previous': None,
        'results': BoardListSerializer(instance=(board,), many=True).data
    }

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_update(auth_user: APIClient, test_user: User, board: Board, board_part: BoardParticipant):
    response = auth_user.put(reverse('board', kwargs={'pk': board.pk}),
                             data=json.dumps({"title": "updated board", "participants": []}),
                             content_type="application/json")
    assert response.status_code == 200
    assert response.data.get('title') == 'updated board'


@pytest.mark.django_db
def test_delete(auth_user: APIClient, board: Board, board_part: BoardParticipant):
    url = reverse('board', kwargs={'pk': board.pk})
    response = auth_user.delete(path=url)

    assert response.status_code == 204
