import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    birthyear = models.DateField()
    deathyear = models.DateField(blank=True, null=True)
    img = models.FileField(null=True)
def __str__(self):
    return self.identity

def get_absolute_url(self):
    return reverse('hero_detail', args=[str(self.id)])
