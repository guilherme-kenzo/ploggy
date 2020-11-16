from django.db import models


class TemperatureData(models.Model):
    humidity = models.FloatField()
    temperature = models.FloatField()
    entry_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['entry_dt'])
        ]

    def to_dict(self):
        return {
            "id": self.id,
            "humidity": self.humidity,
            "temperature": self.temperature,
            "entry_dt": self.entry_dt
        }


class SoundData(models.Model):
    decibels = models.FloatField()
    entry_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['entry_dt'])
        ]
