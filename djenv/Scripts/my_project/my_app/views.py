# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError

from .forms import *
from django.db.models import Q

def department(request):
    if request.method == 'POST':
        instance = None
        try:
            instance = DEPARTMENT.objects.get(d_number=request.POST['d_number'])
        except ObjectDoesNotExist:
            pass
        except MultiValueDictKeyError:
            pass
        form = DepartmentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        else:
            return redirect('/department')
        return redirect('/sel2')

    else:
        form = DepartmentForm()
        return render(request, 'department.html', {'form': form})


def deplocation(request):
    if request.method == 'POST':
        instance = None
        try:
            instance = DEP_LOCATIONS.objects.get(d_number=request.POST['d_number'], d_location=request.POST['d_location'])
        except ObjectDoesNotExist:
            pass
        except MultiValueDictKeyError:
            pass
        form = DepLocationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        else:
            return redirect('/deplocation')
        return redirect('/sel3')

    else:
        form = DepLocationForm()
        return render(request, 'deplocation.html', {'form': form})


def project(request):
    if request.method == 'POST':
        instance = None
        try:
            instance = PROJECT.objects.get(p_number=request.POST['p_number'])
        except ObjectDoesNotExist:
            pass
        except MultiValueDictKeyError:
            pass
        form = ProjectForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        else:
            return redirect('/project')
        return redirect('/sel4')

    else:
        form = ProjectForm()
        return render(request, 'project.html', {'form': form})


def dependent(request):
    if request.method == 'POST':
        instance = None
        try:
            instance = DEPENDENT.objects.get(e_ssn=request.POST['e_ssn'], dependent_name=request.POST['dependent_name'])
        except ObjectDoesNotExist:
            pass
        except MultiValueDictKeyError:
            pass
        form = DependentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        else:
            return redirect('/dependent')
        return redirect('/sel5')

    else:
        form = DependentForm()
        return render(request, 'dependent.html', {'form': form})


def employee(request):
    if request.method == 'POST':
        instance = None
        try:
            instance = EMPLOYEE.objects.get(ssn=request.POST['ssn'])
        except ObjectDoesNotExist:
            pass
        except MultiValueDictKeyError:
            pass
        form = EmployeeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('/')

    else:
        form = EmployeeForm()
        return render(request, 'employee.html', {'form': form})


def workson(request):
    if request.method == 'POST':
        instance = None
        try:
            instance = WORKSON.objects.get(e_ssn=request.POST['e_ssn'], pno=request.POST['pno'])
        except ObjectDoesNotExist:
            pass
        except MultiValueDictKeyError:
            pass
        form = WorksOnForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        else:
            return redirect('/workson')
        return redirect('/sel6')

    else:
        form = WorksOnForm()
        return render(request, 'workson.html', {'form': form})


def sel1(request):
    res = []
    for s in EMPLOYEE.objects.all():
        res += [s]
    return render(request, 'sel1.html', {'res': res})


def sel2(request):
    res = []
    for s in DEPARTMENT.objects.all():
        res += [s]
    return render(request, 'sel2.html', {'res': res})


def sel3(request):
    res = []
    for s in DEP_LOCATIONS.objects.all():
        res += [s]
    return render(request, 'sel3.html', {'res': res})


def sel4(request):
    res = []
    for s in PROJECT.objects.all():
        res += [s]
    return render(request, 'sel4.html', {'res': res})


def sel5(request):
    res = []
    for s in DEPENDENT.objects.all():
        res += [s]
    return render(request, 'sel5.html', {'res': res})


def sel6(request):
    res = []
    for s in WORKSON.objects.all():
        res += [s]
    return render(request, 'sel6.html', {'res': res})


def delete_employee(request):
    try:
        emp = EMPLOYEE.objects.get(ssn=request.POST['title'])
        emp.delete()
    except ObjectDoesNotExist:
        pass
    except MultiValueDictKeyError:
        pass
    return redirect('/sel1')


def delete_department(request):
    try:
        dep = DEPARTMENT.objects.get(d_number=request.POST['title'])
        dep.delete()
    except ObjectDoesNotExist:
        pass
    except MultiValueDictKeyError:
        pass
    return redirect('/sel2')


def delete_deplocation(request):
    try:
        deplo = DEP_LOCATIONS.objects.get(d_number=request.POST['title1'], d_location=request.POST['title2'])
        deplo.delete()
    except ObjectDoesNotExist:
        pass
    except MultiValueDictKeyError:
        pass
    return redirect('/sel3')


def delete_project(request):
    try:
        pro = PROJECT.objects.get(p_number=request.POST['title'])
        pro.delete()
    except ObjectDoesNotExist:
        pass
    except MultiValueDictKeyError:
        pass
    return redirect('/sel4')


def delete_dependent(request):
    try:
        depen = DEPENDENT.objects.get(e_ssn=request.POST['title1'], dependent_name=request.POST['title2'])
        depen.delete()
    except ObjectDoesNotExist:
        pass
    except MultiValueDictKeyError:
        pass
    return redirect('/sel5')


def delete_workson(request):
    try:
        work = WORKSON.objects.get(e_ssn=request.POST['title1'], pno=request.POST['title2'])
        work.delete()
    except ObjectDoesNotExist:
        pass
    except MultiValueDictKeyError:
        pass
    return redirect('/sel6')


def init(request):
    EMPLOYEE.objects.all().delete()
    DEPARTMENT.objects.all().delete()
    DEP_LOCATIONS.objects.all().delete()
    PROJECT.objects.all().delete()
    DEPENDENT.objects.all().delete()

    dep1 = DEPARTMENT(d_name="Research", d_number="5", mgr_start_date="1988-05-22")
    dep2 = DEPARTMENT(d_name="Administration", d_number="4", mgr_start_date="1995-01-01")
    dep3 = DEPARTMENT(d_name="Headquaters", d_number="1", mgr_start_date="1981-06-19")
    dep1.save()
    dep2.save()
    dep3.save()

    deptlo1 = DEP_LOCATIONS(d_number_id="5", d_location="Houston")
    deptlo2 = DEP_LOCATIONS(d_number_id="4", d_location="Stafford")
    deptlo3 = DEP_LOCATIONS(d_number_id="1", d_location="Bellaire")
    deptlo1.save()
    deptlo2.save()
    deptlo3.save()

    emp1 = EMPLOYEE(f_name="John", m_init="B", l_name="Smith", ssn="123456789", b_date="1965-01-09",
                    address="731 Fordren, Houston, TX", sex="M", salary=30000, d_number_id="1")
    emp2 = EMPLOYEE(f_name="Franklin", m_init="T", l_name="Wong", ssn="333445555", b_date="1955-12-08",
                    address="638 Voss, Houston, TX", sex="M", salary=40000, super_ssn_id="123456789", d_number_id="4")
    emp3 = EMPLOYEE(f_name="Alicia", m_init="J", l_name="Zelaya", ssn="999887777", b_date="1968-01-19",
                    address="3321 Castle, Spring, TX", sex="F", salary=25000, super_ssn_id="123456789", d_number_id="5")
    emp1.save()
    emp2.save()
    emp3.save()

    pro1 = PROJECT(p_name="ProductX", p_number="1", p_location="Bellaire", d_number_id="5")
    pro2 = PROJECT(p_name="ProductY", p_number="2", p_location="Sugarland", d_number_id="5")
    pro3 = PROJECT(p_name="ProductZ", p_number="3", p_location="Houston", d_number_id="4")
    pro1.save()
    pro2.save()
    pro3.save()

    work1 = WORKSON(e_ssn_id="123456789", pno_id=3, hours="32.5")
    work2 = WORKSON(e_ssn_id="333445555", pno_id=2, hours="7.5")
    work3 = WORKSON(e_ssn_id="999887777", pno_id=1, hours="40.0")
    work1.save()
    work2.save()
    work3.save()

    depen1 = DEPENDENT(e_ssn_id="333445555", dependent_name="Alice", sex="F", b_date="1985-04-05", relationship="Daughter")
    depen2 = DEPENDENT(e_ssn_id="333445555", dependent_name="Theodore", sex="M", b_date="1983-10-25", relationship="Son")
    depen3 = DEPENDENT(e_ssn_id="333445555", dependent_name="Joy", sex="F", b_date="1958-05-03", relationship="Spouse")
    depen1.save()
    depen2.save()
    depen3.save()

    return redirect('/')