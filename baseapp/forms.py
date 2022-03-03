from dataclasses import field
from django.forms import ModelForm
from .models import EmployeeDataManager, Projects

class EmployeeDataManagerForm(ModelForm):
    class Meta:
        model = EmployeeDataManager
        fields = '__all__'

class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'