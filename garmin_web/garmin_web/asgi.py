# @Author: Manuel Rodriguez <valle>
# @Date:   2019-10-18T16:54:32+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-18T17:15:11+02:00
# @License: Apache License v2.0


"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "garmin_web.settings")

django.setup()
application = get_default_application()
