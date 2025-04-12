from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManufacturerViewSet, FeatureViewSet, CarViewSet

router = DefaultRouter()
router.register('manufacturers', ManufacturerViewSet)
router.register('features', FeatureViewSet)
router.register('cars', CarViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
