from django.db import models
from digb_backend.core.models import BaseModel


class ProgressBarModel(BaseModel):
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()
    order = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
