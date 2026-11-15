from django.db import models

# Create your models here.
class Student(models.Model):
  name=models.CharField(max_length=200)
  email=models.EmailField(unique=True)
  course=models.CharField(max_length=200)
  pass_out_year=models.PositiveIntegerField()
  college=models.CharField(max_length=200)
