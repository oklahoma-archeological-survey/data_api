# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Dokarrs(models.Model):
    obsnum = models.CharField(max_length=7, blank=True)
    class_field = models.CharField(db_column='class', max_length=10, blank=True) # Field renamed because it was a Python reserved word.
    family = models.CharField(max_length=20, blank=True)
    genus = models.CharField(max_length=15, blank=True)
    species = models.CharField(max_length=35, blank=True)
    common_name = models.CharField(db_column='comname' ,max_length=40, blank=True)
    county = models.CharField(max_length=20, blank=True)
    local = models.CharField(max_length=140, blank=True)
    obsvr = models.CharField(max_length=50, blank=True)
    day = models.CharField(max_length=20, blank=True)
    month = models.CharField(max_length=25, blank=True)
    year = models.CharField(max_length=10, blank=True)
    number = models.CharField(max_length=25, blank=True)
    habitat = models.CharField(max_length=250, blank=True)
    remarks = models.CharField(max_length=255, blank=True)
    museum = models.CharField(max_length=100, blank=True)
    citatin = models.CharField(max_length=90, blank=True)
    timestamp = models.DateTimeField(db_column='TIMESTAMP') # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'dokarrs'
        permissions =(("view_task","Can see available tasks"),)

