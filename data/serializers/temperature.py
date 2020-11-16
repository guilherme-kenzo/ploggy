from rest_framework.serializers import ModelSerializer
from data.models import TemperatureData

class TemperatureSerializer(ModelSerializer):

    class Meta:
        model = TemperatureData
        fields = [
            'humidity',
            'temperature',
        ]