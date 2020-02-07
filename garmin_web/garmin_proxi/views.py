# @Author: Manuel Rodriguez <valle>
# @Date:   2019-10-18T01:13:24+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-19T16:32:47+02:00
# @License: Apache License v2.0

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.http import HttpResponse
from garmin_web.settings import DIR_FITs, PYTHON, GARMIN_CONNECT, RECEPTOR
from garmin_proxi.models.garmin_activities import Activities
from fitparse  import FitFile
from  datetime import datetime
import websocket
import json
import os


try:
    import thread
except ImportError:
    import _thread as thread

def update_garmin_data(request):
    thread.start_new_thread(run_update_garmin, (request,))
    return HttpResponse("success")

def get_activities(request):
    activities = Activities.objects.all()
    json_send = []
    for a in activities:
        json_send.append({
            "id": a.id,
            "name": a.name,
            "time": a.elapsed_time.strftime("%H:%M:%S"),
            "laps": a.laps,
            "calories": a.calories,
            "max_hr": a.max_hr,
            "avg_hr": a.avg_hr
        })

    return HttpResponse(json.dumps(json_send, indent=4))


def get_activity_statistics(request, id):

    fitfile = FitFile(os.path.join(DIR_FITs, id+'.fit'))
    control_series = 0
    control_ejercicio = 0
    serie = {
        "tiempo_descanso_serie": 0,
        "tiempo_trabajo_serie": 0,
        "repeticiones_serie": 0,
        "peso_serie": 0,
        "ejercicio": 0,
    }
    ejercicio = {
          'ejercicio': 0,
          "series": []
    }
    ejercicios = []
    for record in fitfile.get_messages('record'):
        # Go through all the data entries in this record
        for record_data in record:
            value = record_data.value

            if record_data.name in serie.keys():
                if type(value) is datetime:
                    value = record_data.value.strftime("%H:%M:%S")
                elif type(value) is not str:
                    value = str(value)
                    serie[record_data.name] = value


            if "control_series" == record_data.name:
                aux = int(value)
                if aux > control_series:
                    control_series = aux
                    ejercicio["ejercicio"] = get_ejercicio_name(serie["ejercicio"])
                    ejercicio["series"].append(serie)
                    serie = {
                        "tiempo_descanso_serie": 0,
                        "tiempo_trabajo_serie": 0,
                        "repeticiones_serie": 0,
                        "peso_serie": 0,
                        "ejercicio": 0,
                    }

            if "control_ejercicio" == record_data.name:
                aux = int(value)
                if aux > control_ejercicio:
                    control_ejercicio = aux
                    ejercicios.append(ejercicio)
                    ejercicio = {
                        'ejercicio': "",
                        'series': []
                    }



    ejercicios.append(ejercicio)
    ejercicio = {
      'ejercicio': "",
      'series': []
      }

    return HttpResponse(json.dumps(ejercicios))


def get_ejercicio_name(index):
    index = int(index)
    if index == 7:
        return "Cardio"
    elif index == 6:
        return "Core"
    elif index == 5:
        return "Hombros"
    elif index == 4:
        return "Brazos"
    elif index == 3:
        return "Piernas"
    elif index == 2:
        return "Espalda"
    elif index == 1:
        return "Pecho"
    return "Cardio"


def run_update_garmin(request):
    os.system(PYTHON+ " "+GARMIN_CONNECT+" --all --download --import --analyze --latest")
    try:
        url = ''.join(['ws://', get_current_site(request).domain, '/ws/', RECEPTOR])
        ws = websocket.create_connection(url)
        ws.send(json.dumps({"message": {"OP": "fin_update"}}))
        ws.close()
    except Exception as e:
        print(e)
