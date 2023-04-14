from rest_framework import serializers
from .models import Status, Tiles

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'status']

class TilesSerializer(serializers.ModelSerializer):
#    tasks = serializers.SlugRelatedField(
#        many = True,
#        read_only = True,
#        slug_field = 'title'
#    )
    status = serializers.SlugRelatedField(
        many = False,
        read_only = True,
        slug_field = 'status'
    )
    class Meta:
        model = Tiles
        fields = ['id', 'launch_date', 'status', 'img']