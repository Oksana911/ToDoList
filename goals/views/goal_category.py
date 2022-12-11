from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination
from goals.models import GoalCategory, Goal
from goals.permissions import GoalCategoryPermission
from goals.serializers.goal_cetegory import GoalCategoryCreateSerializer, GoalCategorySerializer


class GoalCategoryCreateView(CreateAPIView):
    model = GoalCategory
    serializer_class = GoalCategoryCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class GoalCategoryListView(ListAPIView):
    model = GoalCategory
    serializer_class = GoalCategorySerializer
    permission_classes = [GoalCategoryPermission]
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ('board',)
    ordering_fields = ('title', 'created',)
    search_fields = ('title',)

    def get_queryset(self):
        return GoalCategory.objects.filter(
            board__participants__user=self.request.user, is_deleted=False
        )


class GoalCategoryView(RetrieveUpdateDestroyAPIView):
    model = GoalCategory
    serializer_class = GoalCategorySerializer
    permission_classes = [GoalCategoryPermission]

    def get_queryset(self):
        return GoalCategory.objects.filter(
            board__participants__user=self.request.user, is_deleted=False
        )

    def perform_destroy(self, instance):
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.goals.update(status=Goal.Status.archived)  # TODO
            for goal in instance.goals.all():
                goal.status = goal.Status.archived
                goal.save()
        return instance
