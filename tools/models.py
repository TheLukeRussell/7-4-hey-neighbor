from django.db import models
from django.urls import reverse


class Tools(models.Model):
    type = models.CharField(max_length = 30)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('tools:index')