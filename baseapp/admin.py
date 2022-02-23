from django.contrib import admin

from .models import EmployeeDataManager, ManagerData, Projects

# Register your models here.

admin.site.register(EmployeeDataManager)
admin.site.register(ManagerData)
admin.site.register(Projects)