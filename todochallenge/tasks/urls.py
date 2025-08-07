from rest_framework import routers
from tasks.api.task import TaskViewSet


router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = router.urls
