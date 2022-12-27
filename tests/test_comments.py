import pytest
from django.urls import reverse
from factories import CommentFactory
from goals.serializers.goal_comment import CommentSerializer


@pytest.mark.django_db
def test_create(auth_user, test_user, goal):
    url = reverse('comment_create')

    payload = {
        'text': 'new comment',
        'user': test_user.pk,
        'goal': goal.pk,
    }
    response = auth_user.post(
        path=url,
        data=payload
    )
    response_data = response.json()

    assert response.status_code == 201
    assert response_data['text'] == payload['text']


@pytest.mark.django_db
def test_get_one(auth_user, test_user, comment, goal):
    url = reverse('comment', kwargs={'pk': comment.pk})
    response = auth_user.get(path=url)
    response_data = response.json()

    expected_response = {'id': comment.pk,
                         'user': {
                             'id': test_user.pk,
                             'username': 'Petr',
                             'first_name': '',
                             'last_name': '',
                             'email': 'petr@petr.ru'
                         },
                         'created': response.data.get('created'),
                         'updated': response.data.get('updated'),
                         'text': comment.text,
                         'goal': goal.pk}

    assert response.status_code == 200
    assert response_data == expected_response


@pytest.mark.django_db
def test_get_list(auth_user, test_user, goal):
    comments = CommentFactory.create_batch(5, user=test_user, goal=goal)
    expected_response = CommentSerializer(instance=comments, many=True).data
    expected_response_sort = sorted(expected_response, key=lambda x: x['id'], reverse=True)
    url = reverse('comments_list')
    response = auth_user.get(path=url)

    assert response.status_code == 200
    assert response.data == expected_response_sort


@pytest.mark.django_db
def test_update(auth_user, comment, goal):
    url = reverse('comment', kwargs={'pk': comment.pk})
    response = auth_user.put(path=url, data={
        'text': 'updated comment',
        'goal': goal.pk,
    })

    assert response.status_code == 200
    assert response.data.get('text') == 'updated comment'


@pytest.mark.django_db
def test_delete(auth_user, comment):
    url = reverse('comment', kwargs={'pk': comment.pk})
    response = auth_user.delete(path=url)

    assert response.status_code == 204
