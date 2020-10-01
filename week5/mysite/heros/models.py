from django.db import models

# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    birthyear = model.DateField()
    deathyear = model.DateField(blank=True, null=True)
