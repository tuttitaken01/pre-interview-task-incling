from rest_framework import viewsets
from .serializers import StatusSerializer, TilesSerializer
from .models import Status, Tiles

# Create your views here.
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class TilesViewSet(viewsets.ModelViewSet):
    queryset = Tiles.objects.all()
    serializer_class = TilesSerializer

