from rest_framework import routers
from .api import ProjectViewSet, FeaturedProjectViewSet, WebProjectViewSet, HealthProjectViewSet, MechatronicsProjectViewSet, OtherProjectViewSet

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/web-projects', WebProjectViewSet, 'web')
router.register('api/health-projects', HealthProjectViewSet, 'health')
router.register('api/mechatronics-projects', MechatronicsProjectViewSet, 'mechatronics')
router.register('api/other-projects', OtherProjectViewSet, 'other')
router.register('api/featured-projects', FeaturedProjectViewSet, 'featured')


urlpatterns = router.urls