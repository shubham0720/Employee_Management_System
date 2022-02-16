from dataclasses import field
from django.forms import ModelForm
from .models import EmployeeDataManager

class EmployeeDataManagerForm(ModelForm):
    class Meta:
        model = EmployeeDataManager
        fields = '__all__'