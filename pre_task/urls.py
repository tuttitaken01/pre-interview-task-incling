from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from task import views as view_1
from tile import views as view_2

router = routers.DefaultRouter()
router.register(r'tasks', view_1.TaskViewSet)
router.register(r'tiles', view_2.TilesViewSet)

router.register(r'types', view_1.TypeViewSet)
router.register(r'status', view_2.StatusViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('tasks', view_1.task_detail),
    path('tiles', view_2.tile_detail),
    path('tasks/<int:id>', view_1.task_detail),
    path('tiles/<int:id>', view_2.tile_detail),
]
