from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from goals.models import Board, Goal
from goals.permissions import BoardPermissions
from goals.serializers.board import BoardSerializer, BoardCreateSerializer, BoardListSerializer


class BoardCreateView(CreateAPIView):
    model = Board
    serializer_class = BoardCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class BoardListView(ListAPIView):
    model = Board
    serializer_class = BoardListSerializer
    permission_classes = [BoardPermissions]
    pagination_class = LimitOffsetPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    ordering = ('title',)
    search_fields = ('title',)

    def get_queryset(self):
        return self.model.objects.filter(participants__user=self.request.user, is_deleted=False)


class BoardView(RetrieveUpdateDestroyAPIView):
    model = Board
    permission_classes = [BoardPermissions]
    serializer_class = BoardSerializer

    def get_queryset(self):
        return self.model.objects.filter(participants__user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance: Board):
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.categories.update(is_deleted=True)
            Goal.objects.filter(category__board=instance).update(
                status=Goal.Status.archived
            )
        return instance
