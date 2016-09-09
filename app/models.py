"""
Definition of models.
"""

from django.db import models

# Create your models here.
class PI_info(models.Model):
    age = models.DecimalField(max_digits=3,decimal_places=0,default=0)
    time1 = models.DateTimeField(auto_now_add=True)
    gener = models.BooleanField(default=False)
    gener2 = models.BooleanField(default=False)
