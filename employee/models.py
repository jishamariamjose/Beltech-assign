from django.db import models

# Model for Postgresql Employee table.
class EmployeeSchema(models.Model):

    EmployeeCode = models.CharField(unique = True, max_length=20)
    Department = models.CharField(max_length=20)
    DateCreated= models.DateTimeField()
    Score = models.IntegerField()
    