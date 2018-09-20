from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name+' - '+ self.hobby

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    sub= models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name+" "+self.sub
