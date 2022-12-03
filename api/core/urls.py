from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EconomicLessonsViewSet

router = DefaultRouter()
router.register(r"lessons", EconomicLessonsViewSet)

urlpatterns = [path("", include(router.urls))]
