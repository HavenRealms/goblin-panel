from django.db import models

# Create your models here.
class Location(models.Model):
    short_code = models.CharField(max_length=5)
    description = models.CharField(max_length=255)

    def __str__(self):
        return "(" + self.short_code + ") " + self.description