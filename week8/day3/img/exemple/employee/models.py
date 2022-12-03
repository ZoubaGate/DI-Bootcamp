from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_image = models.ImageField(upload_to="images/")
