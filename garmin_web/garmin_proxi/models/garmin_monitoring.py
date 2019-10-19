# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Monitoring(models.Model):
    id = models.AutoField()
    timestamp = models.DateTimeField()
    activity_type = models.CharField(blank=True, null=True)
    intensity = models.IntegerField(blank=True, null=True)
    duration = models.TimeField()
    distance = models.TextField(blank=True, null=True)  # This field type is a guess.
    cum_active_time = models.TimeField()
    active_calories = models.IntegerField(blank=True, null=True)
    steps = models.IntegerField(blank=True, null=True)
    strokes = models.IntegerField(blank=True, null=True)
    cycles = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'monitoring'


class MonitoringClimb(models.Model):
    id = models.AutoField()
    timestamp = models.DateTimeField()
    ascent = models.TextField(blank=True, null=True)  # This field type is a guess.
    descent = models.TextField(blank=True, null=True)  # This field type is a guess.
    cum_ascent = models.TextField(blank=True, null=True)  # This field type is a guess.
    cum_descent = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'monitoring_climb'


class MonitoringHr(models.Model):
    timestamp = models.DateTimeField()
    heart_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'monitoring_hr'


class MonitoringInfo(models.Model):
    timestamp = models.DateTimeField()
    file_id = models.IntegerField()
    activity_type = models.CharField(blank=True, null=True)
    resting_metabolic_rate = models.IntegerField(blank=True, null=True)
    cycles_to_distance = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycles_to_calories = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'monitoring_info'


class MonitoringIntensity(models.Model):
    timestamp = models.DateTimeField()
    moderate_activity_time = models.TimeField()
    vigorous_activity_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'monitoring_intensity'


class Version(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    key = models.CharField()
    value = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version'
