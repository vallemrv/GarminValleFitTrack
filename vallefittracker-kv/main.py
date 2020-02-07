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
from datetime import datetime
import json
import random
import os

SERVER_URL = "localhost:8888"

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
    controller=ObjectProperty()

    def __init__(self, **kargs):
        super(ActividadWdiget, self).__init__(**kargs)
        self.bg_color = RandomColor().get_color()

    def on_bg_color(self, w, v):
        if str(v).startswith("#"):
            self.bg_color = get_color_from_hex(v)
        else:
            self.bg_color = v

    def ver(self):
        if self.controller:
            self.controller(self.tag)

class StatisticsWdiget(AnchorLayout):
    tag = ObjectProperty()
    ejercicio = StringProperty()
    series= ListProperty()
    pesos= ListProperty()
    tiempo_trabajo = ObjectProperty(0)
    tiempo_descanso = ObjectProperty(0)
    tiempo = ObjectProperty(0)

    bg_color=ObjectProperty((.5,.5,.5,1))

    
    def secons_to_string(self, second):
        return datetime.fromtimestamp(int(second)).strftime("%M:%S")


    def __init__(self, **kargs):
        super(StatisticsWdiget, self).__init__(**kargs)
        self.bg_color = RandomColor().get_color()

    def on_bg_color(self, w, v):
        if str(v).startswith("#"):
            self.bg_color = get_color_from_hex(v)
        else:
            self.bg_color = v

    def ver(self):
        if self.controller:
            self.controller(self.tag)



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
            widget.controller = self.find_activity
            self.content_activities.add_widget(widget)

    def find_activity(self, w):
        self.info.text = "Descargando datos de la actidad"
        self.info.show()
        url = os.path.join("http://", SERVER_URL, "garmin",
                "get_activity_statistics", w["id"] )
        UrlRequest(url, on_success=self.ver_activity)

    def ver_activity(self, e, res):
        self.navigate("actividad")
        tiempo_trabajo = 0;
        tiempo_descanso = 0;
        series = []
        peso = []
        self.content_statistics.rm_all_widgets()
        res = json.loads(res)
        for activity in res:
            widget = StatisticsWdiget()
            widget.ejercicio = activity["ejercicio"]
            widget.tag = activity

            for serie in  activity["series"]:
                tiempo_descanso = tiempo_descanso + int(serie["tiempo_descanso_serie"])
                tiempo_trabajo = tiempo_trabajo + int(serie["tiempo_trabajo_serie"])
                series.append(serie["repeticiones_serie"])
                if int(serie["peso_serie"]) > 0:
                    peso.append(serie["peso_serie"])
                elif len(peso) <= 0:
                    peso.append("cuerpo")

            widget.tiempo_trabajo = tiempo_trabajo
            widget.tiempo_descanso = tiempo_descanso
            widget.series = series
            widget.pesos = peso
            widget.tiempo = tiempo_trabajo + tiempo_descanso

            self.content_statistics.add_widget(widget)

    def refresh(self):
        self.info.text = "Buscando cambios en las actidades..."
        self.info.show()
        url = os.path.join("http://", SERVER_URL, "garmin", "update_garmin_data/")
        UrlRequest(url)

    #Esta clase solo implementa onMessage.
    def onMessage(self, message, id):
        if message["message"]["OP"] == "fin_update":
            self.get_activities()

    def get_activities(self):
        self.info.text = "Descargando activities"
        self.info.show()
        UrlRequest(os.path.join("http://", SERVER_URL, "garmin", "get_activities/"),
                   on_success=self.on_success_acitivities)


    def on_success_acitivities(self, e, res):
        self.activities = json.loads(res)



class ValleFitTrackApp(App):
    def build(self):
        ws_controller = ValleFitTrackPage()
        url = os.path.join("ws://", SERVER_URL, "ws", "vallefittracker")
        self.ws = WSManager(url= url, controller=ws_controller)
        return ws_controller

    def on_stop(self):
        self.ws.close()



if __name__ == '__main__':
    ValleFitTrackApp().run()
