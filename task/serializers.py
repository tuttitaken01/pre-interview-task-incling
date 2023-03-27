from rest_framework import serializers
from .models import Tasks, Types


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ('id', 'type')

class TaskSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(
        many = False,
        read_only = True,
        slug_field = 'type'
    )
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'order', 'description', 'type')

