# @Author: Manuel Rodriguez <valle>
# @Date:   2019-10-18T01:43:37+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-18T18:37:02+02:00
# @License: Apache License v2.0

from django.urls import path
from garmin_proxi import views

urlpatterns = [
     path('get_activities/', views.get_activities, name="get_activities"),
     path('get_activity_statistics/<str:id>', views.get_activity_statistics, name="get_activity_statistics"),
     path('update_garmin_data/', views.update_garmin_data, name="update_garmin_data")

]
