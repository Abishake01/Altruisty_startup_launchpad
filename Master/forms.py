from django import forms
from .models import Instructor
from django.core.exceptions import ValidationError
import re

from .models import EmployeeType

class EmployeeTypeForm(forms.ModelForm):
    class Meta:
        model = EmployeeType
        fields = ['name']  # Only the 'name' field is needed for Employee Type
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter department name'}),
        }

from django import forms
from .models import Department,Designation

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']  # Only the department name field is needed now
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter department name'}),
        }


        from .models import Designation

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['name']  # Fields to include in the form

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

    # Custom validations
    