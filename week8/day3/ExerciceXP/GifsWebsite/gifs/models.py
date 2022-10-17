from django.db import models
from datetime import datetime, date
# Create your models here.

class GifModel(models.Model):
    title=models.CharField(max_length=30)
    url=models.URLField()
    create_at=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.title}'
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    gifs= models.ManyToManyField(GifModel,related_name='categories',blank=True)
    
    def __str__(self):
        return f'Category {self.name}'



