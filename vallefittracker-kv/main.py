# @Author: Manuel Rodriguez <valle>
# @Date:   2019-10-16T03:58:04+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-19T16:30:29+02:00
# @License: Apache License v2.0


import kivy
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.network.urlrequest import UrlRequest
from kivy.utils import get_color_from_hex
from components.pagenavigations import PageManager, Page
from ws_connect import WSManager
import json
import random
import os

SERVER_URL = "http://localhost:8888"

class RandomColor():
    colores = ["#F7DC6F", "#A9DFBF", "#AED6F1", "#FDEBD0", "#E8DAEF"]
    last_color = ""

    def get_color(self):
        color = random.choice(self.colores)
        while color == RandomColor.last_color:
            color = random.choice(self.colores)
        RandomColor.last_color = color
        return get_color_from_hex(color)

class ActividadWdiget(AnchorLayout):
    tag = ObjectProperty()
    nombre = StringProperty()
    vueltas= StringProperty()
    tiempo= StringProperty()
    max_hr= StringProperty()
    avg_hr= StringProperty()
    bg_color=ObjectProperty((.5,.5,.5,1))

    def __init__(self, **kargs):
        super(ActividadWdiget, self).__init__(**kargs)
        self.bg_color = RandomColor().get_color()

    def on_bg_color(self, w, v):
        if str(v).startswith("#"):
            self.bg_color = get_color_from_hex(v)
        else:
            self.bg_color = v


class ValleFitTrackPage(PageManager):
    activities = ListProperty([])

    def __init__(self, **kargs):
        super(ValleFitTrackPage, self).__init__(**kargs)
        self.get_activities()

    def on_activities(self, w, v):
        self.content_activities.rm_all_widgets() 
        for i in range(len(v)-1, 0, -1):
            activity = v[i]
            widget = ActividadWdiget()
            widget.nombre = activity["name"]
            widget.tiempo = activity["time"]
            widget.vueltas = str(activity["laps"])
            widget.avg_hr = str(activity["avg_hr"])
            widget.max_hr = str(activity["max_hr"])
            widget.tag = activity
            self.content_activities.add_widget(widget)

    def set_activity(self, w):
        print(w)

    def refresh(self):
        self.info.text = "Buscando cambios en las actidades..."
        self.info.show()
        url = os.path.join(SERVER_URL, "garmin", "update_garmin_data/")
        UrlRequest(url)

    def edit(self):
        pass

    def onOpen(self, id):
        print("El ws esta en conexion.....", id)

    def onMessage(self, message, id):
        if message["message"]["OP"] == "fin_update":
            self.get_activities()

    def get_activities(self):
        self.info.text = "Descargando activities"
        self.info.show()
        UrlRequest(os.path.join(SERVER_URL, "garmin", "get_activities/"),
                   on_success=self.on_success_acitivities)

    def on_success_acitivities(self, e, res):
        self.activities = json.loads(res)



class ValleFitTrackApp(App):
    def build(self):
        ws_controller = ValleFitTrackPage()
        self.ws = WSManager(url= "ws://localhost:8888/ws/vallefittracker", controller=ws_controller)
        return ws_controller

    def on_stop(self):
        self.ws.closed = True


if __name__ == '__main__':
    ValleFitTrackApp().run()
