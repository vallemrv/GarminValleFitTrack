# @Author: Manuel Rodriguez <valle>
# @Date:   2019-10-18T01:24:26+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-18T16:56:17+02:00
# @License: Apache License v2.0



# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activities(models.Model):
    start_lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_long = models.TextField(blank=True, null=True)  # This field type is a guess.
    stop_lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    stop_long = models.TextField(blank=True, null=True)  # This field type is a guess.
    id = models.CharField(max_length=200, db_column='activity_id', primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=200)
    type = models.CharField(blank=True, null=True, max_length=200)
    course_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    stop_time = models.DateTimeField(blank=True, null=True)
    elapsed_time = models.TimeField()
    moving_time = models.TimeField()
    sport = models.CharField(blank=True, null=True, max_length=200)
    sub_sport = models.CharField(blank=True, null=True, max_length=200)
    distance = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycles = models.TextField(blank=True, null=True)  # This field type is a guess.
    laps = models.IntegerField(blank=True, null=True)
    avg_hr = models.IntegerField(blank=True, null=True)
    max_hr = models.IntegerField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    avg_cadence = models.IntegerField(blank=True, null=True)
    max_cadence = models.IntegerField(blank=True, null=True)
    avg_speed = models.TextField(blank=True, null=True)  # This field type is a guess.
    max_speed = models.TextField(blank=True, null=True)  # This field type is a guess.
    ascent = models.TextField(blank=True, null=True)  # This field type is a guess.
    descent = models.TextField(blank=True, null=True)  # This field type is a guess.
    max_temperature = models.TextField(blank=True, null=True)  # This field type is a guess.
    min_temperature = models.TextField(blank=True, null=True)  # This field type is a guess.
    avg_temperature = models.TextField(blank=True, null=True)  # This field type is a guess.
    training_effect = models.TextField(blank=True, null=True)  # This field type is a guess.
    anaerobic_training_effect = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'activities'


class ActivitiesExtraData(models.Model):
    mood = models.CharField(blank=True, null=True, max_length=200)
    condition = models.CharField(blank=True, null=True, max_length=200)
    weather = models.CharField(blank=True, null=True, max_length=200)
    text = models.CharField(blank=True, null=True, max_length=200)
    people = models.CharField(blank=True, null=True, max_length=200)
    activity = models.ForeignKey(Activities, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'activities_extra_data'


class ActivityLaps(models.Model):
    start_lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_long = models.TextField(blank=True, null=True)  # This field type is a guess.
    stop_lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    stop_long = models.TextField(blank=True, null=True)  # This field type is a guess.
    activity = models.ForeignKey(Activities, models.DO_NOTHING)
    lap = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    stop_time = models.DateTimeField(blank=True, null=True)
    elapsed_time = models.TimeField()
    moving_time = models.TimeField()
    distance = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycles = models.TextField(blank=True, null=True)  # This field type is a guess.
    avg_hr = models.IntegerField(blank=True, null=True)
    max_hr = models.IntegerField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    avg_cadence = models.IntegerField(blank=True, null=True)
    max_cadence = models.IntegerField(blank=True, null=True)
    avg_speed = models.TextField(blank=True, null=True)  # This field type is a guess.
    max_speed = models.TextField(blank=True, null=True)  # This field type is a guess.
    ascent = models.TextField(blank=True, null=True)  # This field type is a guess.
    descent = models.TextField(blank=True, null=True)  # This field type is a guess.
    max_temperature = models.TextField(blank=True, null=True)  # This field type is a guess.
    min_temperature = models.TextField(blank=True, null=True)  # This field type is a guess.
    avg_temperature = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'activity_laps'


class ActivityRecords(models.Model):
    activity = models.ForeignKey(Activities, models.DO_NOTHING)
    record = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    position_lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    position_long = models.TextField(blank=True, null=True)  # This field type is a guess.
    distance = models.TextField(blank=True, null=True)  # This field type is a guess.
    cadence = models.IntegerField(blank=True, null=True)
    hr = models.IntegerField(blank=True, null=True)
    alititude = models.TextField(blank=True, null=True)  # This field type is a guess.
    speed = models.TextField(blank=True, null=True)  # This field type is a guess.
    temperature = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'activity_records'


class CycleActivities(models.Model):
    strokes = models.IntegerField(blank=True, null=True)
    vo2_max = models.TextField(blank=True, null=True)  # This field type is a guess.
    activity = models.ForeignKey(Activities, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cycle_activities'


class EllipticalActivities(models.Model):
    steps = models.IntegerField(blank=True, null=True)
    elliptical_distance = models.TextField(blank=True, null=True)  # This field type is a guess.
    activity = models.ForeignKey(Activities, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'elliptical_activities'


class PaddleActivities(models.Model):
    strokes = models.IntegerField(blank=True, null=True)
    avg_stroke_distance = models.TextField(blank=True, null=True)  # This field type is a guess.
    activity = models.ForeignKey(Activities, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'paddle_activities'


class StepsActivities(models.Model):
    steps = models.IntegerField(blank=True, null=True)
    avg_pace = models.TimeField()
    avg_moving_pace = models.TimeField()
    max_pace = models.TimeField()
    avg_steps_per_min = models.IntegerField(blank=True, null=True)
    max_steps_per_min = models.IntegerField(blank=True, null=True)
    avg_step_length = models.TextField(blank=True, null=True)  # This field type is a guess.
    avg_vertical_ratio = models.TextField(blank=True, null=True)  # This field type is a guess.
    avg_vertical_oscillation = models.TextField(blank=True, null=True)  # This field type is a guess.
    avg_gct_balance = models.TextField(blank=True, null=True)  # This field type is a guess.
    avg_ground_contact_time = models.TimeField()
    avg_stance_time_percent = models.TextField(blank=True, null=True)  # This field type is a guess.
    vo2_max = models.TextField(blank=True, null=True)  # This field type is a guess.
    activity = models.ForeignKey(Activities, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'steps_activities'


class Version(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    key = models.CharField(max_length=200)
    value = models.CharField(blank=True, null=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'version'
