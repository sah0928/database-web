from django.forms import ModelForm
from .models import *


class EmployeeForm(ModelForm):
    class Meta:
        model = EMPLOYEE
        fields = ['f_name', 'm_init', 'l_name', 'ssn', 'b_date', 'address', 'sex', 'salary', 'super_ssn', 'd_number']


class DepartmentForm(ModelForm):
    class Meta:
        model = DEPARTMENT
        fields = ['d_name', 'd_number', 'mgr_ssn', 'mgr_start_date']


class DepLocationForm(ModelForm):
    class Meta:
        model = DEP_LOCATIONS
        fields = ['d_number', 'd_location']


class ProjectForm(ModelForm):
    class Meta:
        model = PROJECT
        fields = ['p_name', 'p_number', 'p_location', 'd_number']


class DependentForm(ModelForm):
    class Meta:
        model = DEPENDENT
        fields = ['e_ssn', 'dependent_name', 'sex', 'b_date', 'relationship']


class WorksOnForm(ModelForm):
    class Meta:
        model = WORKSON
        fields = ['e_ssn', 'pno', 'hours']