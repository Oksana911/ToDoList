import pytest
from django.urls import reverse
from goals.serializers.goal_cetegory import GoalCategorySerializer
from factories import CategoryFactory


@pytest.mark.django_db
def test_create(auth_user, test_user, board, board_part):
    url = reverse('cat_create')

    payload = {
        'title': 'new category',
        'user': test_user.pk,
        'board': board.pk,
    }
    response = auth_user.post(
        path=url,
        data=payload
    )
    response_data = response.json()

    assert response.status_code == 201
    assert response_data['title'] == payload['title']


@pytest.mark.django_db
def test_get_one(auth_user, test_user, category, board):
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
def test_get_list(auth_user, test_user, board):
    categories = CategoryFactory.create_batch(5, user=test_user, board=board)
    expected_response = GoalCategorySerializer(categories, many=True).data
    url = reverse('cat_list')
    response = auth_user.get(path=url)

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_update(auth_user, category, board):
    url = reverse('cat', kwargs={'pk': category.pk})
    response = auth_user.put(path=url, data={
        'title': 'updated category',
        'board': board.pk,
    })

    assert response.status_code == 200
    assert response.data.get('title') == 'updated category'


@pytest.mark.django_db
def test_delete(auth_user, category):
    url = reverse('cat', kwargs={'pk': category.pk})
    response = auth_user.delete(path=url)

    assert response.status_code == 204
