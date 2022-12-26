import pytest
from django.urls import reverse
from factories import BoardFactory
from goals.serializers.board import BoardSerializer


@pytest.mark.django_db
def test_create(auth_user, test_user):
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
def test_get_one(auth_user, test_user, board, board_part):
    url = reverse('board', kwargs={'pk': board.pk})
    response = auth_user.get(path=url)
    response_data = response.json()

    expected_response = BoardSerializer(board).data

    assert response.status_code == 200
    assert response_data == expected_response


@pytest.mark.django_db
def test_get_list(auth_user, test_user, board):
    boards = BoardFactory.create_batch(5)
    expected_response = BoardSerializer(boards, many=True).data

    url = reverse('boards_list')
    response = auth_user.get(path=url)

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_update(auth_user, test_user, board, board_part):
    url = reverse('board', kwargs={'pk': board.pk})
    response = auth_user.put(path=url, data={
        'title': 'updated board',
        'participants': board.board_part,
    })

    assert response.status_code == 200
    assert response.data.get('title') == 'updated board'


@pytest.mark.django_db
def test_delete(auth_user, board, board_part):
    url = reverse('board', kwargs={'pk': board.pk})
    response = auth_user.delete(path=url)

    assert response.status_code == 204
