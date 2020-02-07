# @Author: Manuel Rodriguez <valle>
# @Date:   2019-10-18T01:11:12+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-18T17:05:36+02:00
# @License: Apache License v2.0



"""
WSGI config for garmin_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings = os.environ["settins_garmin_poxi"] if "settins_garmin_poxi" in os.environ else "settings"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'garmin_web.'+ settings)

application = get_wsgi_application()
