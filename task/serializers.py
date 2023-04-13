from rest_framework import serializers
from .models import Tasks, Types


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ('id', 'type')

class TaskSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(
        many = True,
        read_only = True,
        slug_fields = ('type', 'tile_id')
    )
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'order', 'description', 'type', 'tile_id')

