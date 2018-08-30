from rest_framework import routers
from api.views import TodoViewSet, OrgViewSet


router = routers.SimpleRouter()
router.register('todo', TodoViewSet, base_name='todo')
router.register('org', OrgViewSet, base_name='org')

urlpatterns = router.urls
