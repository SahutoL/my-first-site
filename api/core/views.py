from rest_framework import viewsets
from .serializers import EconomicLessonsSerializer
from .models import EconomicLessons


class EconomicLessonsViewSet(viewsets.ModelViewSet):
    serializer_class = EconomicLessonsSerializer
    queryset = EconomicLessons.objects.all()
