from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters, permissions
from rest_framework.pagination import LimitOffsetPagination
from goals.models import GoalComment
from goals.permissions import CommentPermission
from goals.serializers.goal_comment import CommentCreateSerializer, CommentSerializer


class CommentCreateView(CreateAPIView):
    model = GoalComment
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentsListView(ListAPIView):
    model = GoalComment
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]
    pagination_class = LimitOffsetPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = ('goal',)
    ordering = ('-created',)

    def get_queryset(self):
        return self.model.objects.filter(goal__category__board__participants__user=self.request.user)


class CommentView(RetrieveUpdateDestroyAPIView):
    model = GoalComment
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]

    def get_queryset(self):
        return self.model.objects.filter(goal__category__board__participants__user=self.request.user)
