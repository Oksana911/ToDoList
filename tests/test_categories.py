import pytest
from django.urls import reverse
from core.models import User
from goals.models import Board, BoardParticipant, GoalCategory
from goals.serializers.goal_cetegory import GoalCategorySerializer
from factories import CategoryFactory
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create(auth_user: APIClient, test_user: User, board: Board, board_part: BoardParticipant):
    url = reverse('cat_create')

    payload = {
        'title': 'new category',
        'user': test_user.pk,
        'board': board.pk,
    }
    response = auth_user.post(path=url, data=payload)
    response_data = response.json()

    assert response.status_code == 201
    assert response_data['title'] == payload['title']


@pytest.mark.django_db
def test_get_one(auth_user: APIClient, test_user: User, category: GoalCategory, board: Board):
    url = reverse('cat', kwargs={'pk': category.pk})
    response = auth_user.get(path=url)
    response_data = response.json()

    expected_response = {'id': category.pk,
                         'user': {
                             'id': test_user.pk,
                             'username': 'Petr',
                             'first_name': '',
                             'last_name': '',
                             'email': 'petr@petr.ru'
                         },
                         'created': response.data.get('created'),
                         'updated': response.data.get('updated'),
                         'title': category.title,
                         'is_deleted': False,
                         'board': board.pk}

    assert response.status_code == 200
    assert response_data == expected_response


@pytest.mark.django_db
def test_get_list(auth_user: APIClient, test_user: User, board: Board, board_part: BoardParticipant):
    categories = CategoryFactory.create_batch(5, user=test_user, board=board)
    expected_response = GoalCategorySerializer(instance=categories, many=True).data
    expected_response_sort = sorted(expected_response, key=lambda x: x['created'])
    expected_response_sort = sorted(expected_response_sort, key=lambda x: x['title'])

    response = auth_user.get(reverse('cat_list'))

    assert response.status_code == 200
    assert response.data == expected_response_sort


@pytest.mark.django_db
def test_update(auth_user: APIClient, category: GoalCategory, board: Board):
    url = reverse('cat', kwargs={'pk': category.pk})
    response = auth_user.put(path=url, data={
        'title': 'updated category',
        'board': board.pk,
    })

    assert response.status_code == 200
    assert response.data.get('title') == 'updated category'


@pytest.mark.django_db
def test_delete(auth_user: APIClient, category: GoalCategory):
    url = reverse('cat', kwargs={'pk': category.pk})
    response = auth_user.delete(path=url)

    assert response.status_code == 204
