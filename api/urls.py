from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProcessedImageViewSet

router = DefaultRouter()
router.register(r'images', ProcessedImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]