from rest_framework import viewsets
from .serializers import TypeSerializer, TaskSerializer
from .models import Types, Tasks

# Create your views here.
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypeSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer