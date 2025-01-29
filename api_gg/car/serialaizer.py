from rest_framework.serializers import ModelSerializer
from .models import Car


class CarSerialaizer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'