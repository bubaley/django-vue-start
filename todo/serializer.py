from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from todo.models import Tag, Todo


class TagSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Tag
        fields = ('title', 'color', 'id')


class TodoListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta(object):
        model = Todo
        fields = ('id', 'title', 'completed', 'date', 'tags')


class TodoDetailSerializer(WritableNestedModelSerializer):

    tags = TagSerializer(many=True)

    class Meta(object):
        model = Todo
        fields = ('id', 'title', 'description', 'completed', 'date', 'tags')
