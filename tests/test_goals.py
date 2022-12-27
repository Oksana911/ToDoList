from datetime import datetime
import pytest
from django.urls import reverse
from core.models import User
from goals.models import GoalCategory, BoardParticipant, Goal
from goals.serializers.goal import GoalSerializer
from factories import GoalFactory
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create(auth_user: APIClient, category: GoalCategory, board_part: BoardParticipant):
    url = reverse('goal_create')
    test_date = str(datetime.now().date())
    payload = {
        'title': 'new goal',
        'category': category.pk,
        'description': '',
        'due_date': test_date
    }
    response = auth_user.post(
        path=url,
        data=payload
    )
    response_data = response.json()

    assert response.status_code == 201
    assert response_data['title'] == payload['title']


@pytest.mark.django_db
def test_get_one(auth_user: APIClient, test_user: User, category: GoalCategory, board_part: BoardParticipant,
                 goal: Goal):
    url = reverse('goal', kwargs={'pk': goal.pk})
    response = auth_user.get(path=url)
    response_data = response.json()

    expected_response = {'id': goal.pk,
                         'user': {
                             'id': test_user.pk,
                             'username': 'Petr',
                             'first_name': '',
                             'last_name': '',
                             'email': 'petr@petr.ru'
                         },
                         'created': response.data.get('created'),
                         'updated': response.data.get('updated'),
                         'title': goal.title,
                         'description': None,
                         'due_date': None,
                         'status': 1,
                         'priority': 2,
                         'category': category.pk
                         }

    assert response.status_code == 200
    assert response_data == expected_response


@pytest.mark.django_db
def test_get_list(auth_user: APIClient, test_user: User, category: GoalCategory):
    goals = GoalFactory.create_batch(5, category=category, user=test_user)
    expected_response = GoalSerializer(goals, many=True).data
    url = reverse('goals_list')
    response = auth_user.get(path=url)

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_update(auth_user: APIClient, goal: Goal, category: GoalCategory):
    url = reverse('goal', kwargs={'pk': goal.pk})
    response = auth_user.put(path=url, data={
        'title': 'updated goal',
        'category': category.pk,
    })

    assert response.status_code == 200
    assert response.data.get('title') == 'updated goal'


@pytest.mark.django_db
def test_delete(auth_user: APIClient, goal: Goal):
    url = reverse('goal', kwargs={'pk': goal.pk})
    response = auth_user.delete(path=url)

    assert response.status_code == 204
