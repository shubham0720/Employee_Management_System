from django.db import models

# Create your models here.

class EmployeeDataManager(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=20)
    employee_age = models.IntegerField()
    employee_addr = models.CharField(max_length=100)
    employee_dept = models.CharField(max_length=20)
    employee_start_date = models.DateField()
