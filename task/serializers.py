from rest_framework import serializers
from .models import Tasks, Types


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ('id', 'type')

class TaskSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(
        many = False,
        slug_field ='type',
        queryset = Types.objects.all()
    )
    class Meta:
        model = Tasks
        fields = '__all__'
        #['id', 'title', 'order', 'description', 'type', 'tile_id', 'img']

