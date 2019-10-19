# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attributes(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    key = models.CharField()
    value = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attributes'


class DailyExtraData(models.Model):
    mood = models.CharField(blank=True, null=True)
    condition = models.CharField(blank=True, null=True)
    weather = models.CharField(blank=True, null=True)
    text = models.CharField(blank=True, null=True)
    people = models.CharField(blank=True, null=True)
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'daily_extra_data'


class DailySummary(models.Model):
    day = models.DateField()
    hr_min = models.IntegerField(blank=True, null=True)
    hr_max = models.IntegerField(blank=True, null=True)
    rhr = models.IntegerField(blank=True, null=True)
    stress_avg = models.IntegerField(blank=True, null=True)
    step_goal = models.IntegerField(blank=True, null=True)
    steps = models.IntegerField(blank=True, null=True)
    moderate_activity_time = models.TimeField()
    vigorous_activity_time = models.TimeField()
    intensity_time_goal = models.TimeField()
    floors_up = models.TextField(blank=True, null=True)  # This field type is a guess.
    floors_down = models.TextField(blank=True, null=True)  # This field type is a guess.
    floors_goal = models.TextField(blank=True, null=True)  # This field type is a guess.
    distance = models.TextField(blank=True, null=True)  # This field type is a guess.
    calories_goal = models.IntegerField(blank=True, null=True)
    calories_total = models.IntegerField(blank=True, null=True)
    calories_bmr = models.IntegerField(blank=True, null=True)
    calories_active = models.IntegerField(blank=True, null=True)
    calories_consumed = models.IntegerField(blank=True, null=True)
    description = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_summary'


class DeviceInfo(models.Model):
    id = models.AutoField()
    timestamp = models.DateTimeField()
    file = models.ForeignKey('Files', models.DO_NOTHING, blank=True, null=True)
    serial_number = models.ForeignKey('Devices', models.DO_NOTHING, db_column='serial_number')
    device_type = models.CharField(blank=True, null=True)
    software_version = models.CharField(blank=True, null=True)
    cum_operating_time = models.TimeField()
    battery_voltage = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'device_info'


class Devices(models.Model):
    serial_number = models.AutoField()
    timestamp = models.DateTimeField(blank=True, null=True)
    manufacturer = models.CharField(blank=True, null=True)
    product = models.CharField(blank=True, null=True)
    hardware_version = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices'


class Files(models.Model):
    id = models.CharField()
    name = models.CharField(blank=True, null=True)
    type = models.CharField()
    serial_number = models.ForeignKey(Devices, models.DO_NOTHING, db_column='serial_number', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'


class RestingHr(models.Model):
    day = models.DateField()
    resting_heart_rate = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'resting_hr'


class Sleep(models.Model):
    day = models.DateField()
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    total_sleep = models.TimeField()
    deep_sleep = models.TimeField()
    light_sleep = models.TimeField()
    rem_sleep = models.TimeField()
    awake = models.TimeField()

    class Meta:
        managed = False
        db_table = 'sleep'


class SleepEvents(models.Model):
    id = models.AutoField()
    timestamp = models.DateTimeField(blank=True, null=True)
    event = models.CharField(blank=True, null=True)
    duration = models.TimeField()

    class Meta:
        managed = False
        db_table = 'sleep_events'


class Stress(models.Model):
    timestamp = models.DateTimeField()
    stress = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stress'


class Version(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    key = models.CharField()
    value = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version'


class Weight(models.Model):
    day = models.DateField()
    weight = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'weight'
