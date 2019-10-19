# @Author: Manuel Rodriguez <valle>
# @Date:   2019-10-18T01:35:47+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-18T01:49:30+02:00
# @License: Apache License v2.0


from garmin_proxi.models.garmin_activities import Activities, ActivitiesExtraData

class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        """ reading SomeModel from otherdb """
        if model in [Activities, ActivitiesExtraData]:
            return 'garmin_activities'
        return None

    def db_for_write(self, model, **hints):
        """ writing SomeModel to otherdb """
        if model in [Activities, ActivitiesExtraData]:
            return 'garmin_activities'
        return None
