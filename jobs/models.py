from django.db import models
from django.utils import timezone

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    image_url = models.URLField(
        max_length=500,
        default="https://via.placeholder.com/300x200.png?text=Job+Image"
    )

    def __str__(self):
        return self.title
