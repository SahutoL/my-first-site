from rest_framework import serializers
from .models import EconomicLessons


class EconomicLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicLessons
        fields = (
            "id",
            "title",
            "info",
            "detail",
        )
