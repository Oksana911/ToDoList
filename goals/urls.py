from django.urls import path
from goals.views.goal_category_views import GoalCategoryCreateView, GoalCategoryView, GoalCategoryListView
from goals.views.goal_views import GoalCreateView, GoalListView, GoalView

urlpatterns = [
    path('goal_category/create', GoalCategoryCreateView.as_view(), name='cat_create'),
    path('goal_category/list', GoalCategoryListView.as_view(), name='cat_list'),
    path('goal_category/<pk>', GoalCategoryView.as_view(), name='cat'),

    path('goal/create', GoalCreateView.as_view(), name='goal_create'),
    path('goal/list', GoalListView.as_view(), name='goal_list'),
    path('goal/<pk>', GoalView.as_view(), name='goal'),
]


