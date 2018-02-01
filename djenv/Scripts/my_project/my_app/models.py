# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class EMPLOYEE(models.Model):
    class Meta:
        db_table = 'company_employee'

    f_name = models.CharField(max_length=20)
    m_init = models.CharField(max_length=5)
    l_name = models.CharField(max_length=20)
    ssn = models.CharField(max_length=9, primary_key=True)
    b_date = models.DateField()
    address = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=(('F','Female'),('M','Male')))
    salary = models.IntegerField()
    super_ssn = models.ForeignKey('EMPLOYEE', blank=True, null=True, on_delete=models.SET_NULL)
    d_number = models.ForeignKey('DEPARTMENT', blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return str(self.ssn)


class DEPARTMENT(models.Model):
    class Meta:
        db_table = 'company_department'

    d_name = models.CharField(max_length=20, unique=True)
    d_number = models.CharField(max_length=2, primary_key=True)
    mgr_ssn = models.ForeignKey('EMPLOYEE',  blank=True, null=True, on_delete=models.SET_NULL)
    mgr_start_date = models.DateField()

    def __unicode__(self):
        return str(self.d_number) + " : " + self.d_name


class DEP_LOCATIONS(models.Model):
    class Meta:
        db_table = 'company_deptlocation'
        unique_together = (("d_number", "d_location"),)

    d_number = models.ForeignKey('DEPARTMENT')
    d_location = models.CharField(max_length=20)

    def __unicode__(self):
        return str(self.d_number) + " : " + self.d_location


class PROJECT(models.Model):
    class Meta:
        db_table = 'company_project'

    p_name = models.CharField(max_length=20)
    p_number = models.CharField(max_length=20, primary_key=True)
    p_location = models.CharField(max_length=20)
    d_number = models.ForeignKey('DEPARTMENT')

    def __unicode__(self):
        return str(self.p_number) + " : " + self.p_name


class DEPENDENT(models.Model):
    class Meta:
        db_table = 'company_dependent'
        unique_together = (("e_ssn", "dependent_name"),)

    e_ssn = models.ForeignKey('EMPLOYEE', blank=True, null=True)
    dependent_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1)
    b_date = models.DateField()
    relationship = models.CharField(max_length=20)

    def __unicode__(self):
        return self.dependent_name + ", " + self.relationship.lower() + " of " + str(self.e_ssn)


class WORKSON(models.Model):
    class Meta:
        db_table = 'company_workson'
        unique_together = (("e_ssn", "pno"),)

    e_ssn = models.ForeignKey('EMPLOYEE')
    pno = models.ForeignKey('PROJECT')
    hours = models.CharField(max_length=20)

    def __unicode__(self):
        return "Essn: " + str(self.e_ssn) + ", Pno: " + str(self.pno)