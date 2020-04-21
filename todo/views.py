from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Tag, Todo
from .serializer import TodoDetailSerializer, TodoListSerializer, TagSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_classes = {
        'list': TodoListSerializer,
    }

    @action(detail=True, methods=['post'])
    def change_completed(self, request, pk=None):
        todo = self.get_object()
        todo.completed = not todo.completed
        todo.save()
        return Response({'completed': todo.completed}, status=status.HTTP_200_OK)

    def get_queryset(self):
        tag = self.request.query_params.get('tagFilter')
        search = self.request.query_params.get('search')
        queryset = Todo.objects.filter(owner=self.request.user)
        if tag:
            queryset = queryset.filter(tags__id=tag)
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, TodoDetailSerializer)


class TagViewSet(viewsets.ModelViewSet):

    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
