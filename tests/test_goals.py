from datetime import datetime
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_goal(auth_user, category, board_part):
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
    assert response.status_code == 201
    assert response.json()['title'] == payload['title']
