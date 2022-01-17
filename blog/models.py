from django.db import models
from django.forms import IntegerField

# Create your models here.
class post(models.Model):
    id = IntegerField()
    title = models.CharField(max_length=150)
    desc = models.TextField()
    img = models.ImageField()
    def __str__(self):
        return self.title