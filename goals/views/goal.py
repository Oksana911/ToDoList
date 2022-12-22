from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters, permissions
from rest_framework.pagination import LimitOffsetPagination
from goals.filters import GoalDateFilter
from goals.models import Goal
from goals.permissions import GoalPermission
from goals.serializers.goal import GoalCreateSerializer, GoalSerializer


class GoalCreateView(CreateAPIView):
    model = Goal
    serializer_class = GoalCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class GoalListView(ListAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [GoalPermission]
    pagination_class = LimitOffsetPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = GoalDateFilter
    ordering_fields = ('-priority', 'due_date')
    ordering = ('-priority',)
    search_fields = ('title',)

    def get_queryset(self):
        return self.model.objects.filter(category__board__participants__user=self.request.user
                                         ).exclude(status=self.model.Status.archived)


class GoalView(RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [GoalPermission]

    def get_queryset(self):
        return self.model.objects.filter(category__board__participants__user=self.request.user
                                         ).exclude(status=self.model.Status.archived)

    def perform_destroy(self, instance: Goal):
        instance.status = self.model.Status.archived
        instance.save()
        return instance
