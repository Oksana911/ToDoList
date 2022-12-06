from django.urls import path, include
from goals.views import GoalCategoryCreateView, GoalCategoryView

urlpatterns = [
    path('goal_category/create', GoalCategoryCreateView.as_view(), name='cat_create'),
    path('goal_category/list', GoalCategoryCreateView.as_view(), name='cat_list'),
    path('goal_category/<pk>', GoalCategoryView.as_view(), name='cat'),
]


