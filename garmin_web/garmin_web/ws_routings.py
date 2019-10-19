# @Author: Manuel Rodriguez <valle>
# @Date:   2019-10-18T16:53:35+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-18T17:26:43+02:00
# @License: Apache License v2.0

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import garmin_proxi.ws_routings

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            garmin_proxi.ws_routings.websocket_urlpatterns
        )
    ),
})
