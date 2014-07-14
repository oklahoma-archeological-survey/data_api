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

class Doe(models.Model):
    county = models.CharField(max_length=120, blank=True)
    site_number = models.CharField(max_length=12, blank=True)
    dertermination = models.DateField(db_column='dertermination_date', blank=True, null=True)
    referent = models.CharField(max_length=150, blank=True)
    agency = models.CharField(max_length=150, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'doe'

