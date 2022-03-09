from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    webSite = models.URLField(max_length=100)
    foundation = models.PositiveIntegerField()


class Employee(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)