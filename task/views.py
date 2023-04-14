from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TypeSerializer, TaskSerializer
from .models import Types, Tasks

# Create your views here.
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypeSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def task_detail(request, task_id=None):
    if request.method == 'GET':
        if task_id is not None:
            try:
                task = Tasks.objects.get(task_id=task_id)
            except Tasks.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TaskSerializer(task, context={'request': request})
            return Response(serializer.data)
        else:
            tasks = Tasks.objects.all()
            serializer = TaskSerializer(tasks, many=True, context={'request':request})
            return Response(serializer.data)

    elif request.method == 'POST':
        id = request.data.get('type')
        try:
            task_type = Types.object.get(type_id=id)
        except Types.DoesNotExist:
            return Response({'error': 'Invalid type id'}, status.status.HTTP_400_BAD_REQUEST)
        request.data['type'] = task_type.type_id

        serializer = TaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        if task_id is not None:
            try:
                task = Tasks.objects.get(task_id=task_id)
            except Tasks.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TaskSerializer(task, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if task_id is not None:
            try:
                task = Tasks.objects.get(task_id=task_id)
            except Tasks.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
