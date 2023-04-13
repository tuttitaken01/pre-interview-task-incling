from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StatusSerializer, TilesSerializer
from .models import Status, Tiles

# Create your views here.
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class TilesViewSet(viewsets.ModelViewSet):
    queryset = Tiles.objects.all()
    serializer_class = TilesSerializer


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def tile_detail(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                tile = Tiles.objects.get(pk=pk)
            except Tiles.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TilesSerializer(tile, context={'request': request})
            return Response(serializer.data)
        else:
            tiles = Tiles.objects.all()
            serializer = TilesSerializer(tiles, many=True, context={'request': request})
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TilesSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        if pk is not None:
            try:
                tile = Tiles.objects.get(pk=pk)
            except Tiles.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TilesSerializer(tile, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tile = Tiles.objects.get(pk=pk)
            except Tiles.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            tile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)