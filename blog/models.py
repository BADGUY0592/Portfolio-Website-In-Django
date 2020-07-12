from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(("Date"),default="django.utils.timezone.now")
    urls = models.URLField(blank=True,max_length=50)

    def __str__(self):
        return self.title
