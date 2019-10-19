# @Author: Manuel Rodriguez <valle>
# @Date:   2019-10-18T17:24:54+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-18T17:58:25+02:00
# @License: Apache License v2.0
from django.urls import path
from garmin_proxi import consumers
websocket_urlpatterns=[
     path("ws/<receptor>", consumers.ValleFitTrackConsumer)
]
