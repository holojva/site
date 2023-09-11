from django.db import models

# Create your models here.
class MainModel(models.Model) :
    header = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(null=True, blank=True)
    status = models.BooleanField()
    class Meta :
        ordering = ["-id"]