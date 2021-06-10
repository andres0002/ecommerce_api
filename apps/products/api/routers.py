from rest_framework.routers import DefaultRouter
from apps.products.api.views.viewsets import ProductViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='products')

urlpatterns = router.urls