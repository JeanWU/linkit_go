"""
Definition of models.
"""

from django.db import models

# Create your models here.
class info_7688(models.Model):
    age = models.DecimalField(max_digits=3,decimal_places=0,default=0)
    time1 = models.DateTimeField(auto_now_add=True)
    gender = models.BooleanField(default=False)
    from django.contrib.auth.models import User
    user = models.ForeignKey(User)  #資料屬於哪個使用者

    #def __str__(self):
    #    return self.name

'''for upload picture
class Document(models.Model):
    docfile = models.FileField(upload_to='image')
'''
