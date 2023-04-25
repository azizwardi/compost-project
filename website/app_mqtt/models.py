from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    temperature = models.BigIntegerField()
    humidity = models.BigIntegerField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'Temperature: {self.temperature}, Humidity: {self.humidity}, Published: {self.published_date}'