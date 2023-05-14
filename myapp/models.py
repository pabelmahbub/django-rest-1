from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=30, default='')
    profession = models.CharField(max_length=30, default='')
    
    def __str__(self):
        return self.name
