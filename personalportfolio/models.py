from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='personalportfolio')
    urls = models.URLField(blank=True,max_length=50)

    def __str__(self):
        return self.title
