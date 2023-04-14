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
def tile_detail(request, tile_id=None):
    if request.method == 'GET':
        if tile_id is not None:
            try:
                tile = Tiles.objects.get(tile_id=tile_id)
            except Tiles.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TilesSerializer(tile, context={'request': request})
            return Response(serializer.data)
        else:
            tiles = Tiles.objects.all()
            serializer = TilesSerializer(tiles, many=True, context={'request': request})
            return Response(serializer.data)

    elif request.method == 'POST':
        id = request.data.get('status')
        try:
            tile_status = Status.object.get(status_id=id)
        except Status.DoesNotExist:
            return Response({'error': 'Invalid status'}, status.status.HTTP_400_BAD_REQUEST)
        request.data['status'] = tile_status
        
        serializer = TilesSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        if tile_id is not None:
            try:
                tile = Tiles.objects.get(tile_id=tile_id)
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
        if tile_id is not None:
            try:
                tile = Tiles.objects.get(tile_id=tile_id)
            except Tiles.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            tile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)