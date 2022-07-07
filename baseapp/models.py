from importlib.metadata import requires
from django.db import models

# Create your models here.

class ManagerData(models.Model):
    manager_id = models.IntegerField()
    manager_name = models.CharField(max_length=200)
    manager_age = models.IntegerField()

    def __str__(self):
        return self.manager_name

class EmployeeDataManager(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=20)
    employee_age = models.IntegerField()
    employee_addr = models.CharField(max_length=100)
    employee_dept = models.CharField(max_length=20)
    employee_start_date = models.DateField(auto_now_add=True)
    isManager = models.BooleanField(default=False)
    manager_id = models.ForeignKey(ManagerData, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.employee_name

    class Meta:
        ordering = ['-employee_start_date']

class Projects(models.Model):
    project_id = models.IntegerField()
    project_name = models.CharField(max_length=200)
    manager_id = models.ForeignKey(ManagerData, on_delete=models.CASCADE)
    project_field = models.CharField(max_length=200)
    project_start_date = models.DateField()
    project_end_date = models.DateField()

    def __str__(self):
        return self.project_name


