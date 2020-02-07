# @Author: Manuel Rodriguez <valle>
# @Date:   11-Jun-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-19T16:10:59+02:00
# @License: Apache license vesion 2.0

from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty
from kivy.clock import Clock
from kivy.logger import Logger
from functools import partial

import sys
import websocket
import json
import time
import threading


# Clase encargada para recirbir e enviar mensajes al websocket
class WSManager(EventDispatcher):
    closed = BooleanProperty(False)

    # El contructor tiene los parametros de la direccion del sevidor websocket y un controlador el cual
    # maneja los eventos que genera el ws_manager.
    # el controller tiene que implenetar o no: onMessage, onClose, onOpen, onError.
    def __init__(self, url, controller):
        self.controller = controller
        self.url = url
        threading.Thread(target=self.run_websoker).start()

    def send(self, mensaje):
        if self.ws:
            self.ws.send(json.dumps(mensaje))

    def on_closed(self, w, v):
        if self.closed:
            self.ws.close()

    #llamada para cerrar el websocket pues es de conexion contiuada.
    def close(self):
        self.closed = True
        self.ws.close()

    def on_message(self, message):
        if self.controller and hasattr(self.controller, "onMessage"):
            try:
                message = json.loads(message)
            except:
                pass
            Clock.schedule_once(partial(self.controller.onMessage, message), 0.5)
        else:
            Logger.info("ValleFit: No implementado onMessage en el controlador "+message)

    def on_error(self, error):
        if self.controller and hasattr(self.controller, "onError"):
            Clock.schedule_once(partial(self.controller.onError, error), 0.5)
        else:
            Logger.info("ValleFit: Error en ws, no implementado onError: ", error)

    def on_close(self):
        if self.controller and hasattr(self.controller, "onClose"):
            Clock.schedule_once(partial(self.controller.onClose), 0.5)
        else:
            Logger.info("ValleFit: Cerrado el ws, no implementado onClose")

    def on_open(self):
        if self.controller and hasattr(self.controller, "onOpen"):
            Clock.schedule_once(partial(self.controller.onOpen), 0.5)
        else:
            Logger.info("ValleFit: Abierto el ws, no implementado onOpen")


    def run_websoker(self):
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message = self.on_message,
                                         on_error = self.on_error,
                                         on_close = self.on_close)
        self.ws.on_open = self.on_open

        while not self.closed:
            self.ws.run_forever()
            time.sleep(1)
