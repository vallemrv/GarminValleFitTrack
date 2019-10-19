using Toybox.Time;
using Toybox.Timer;
using Toybox.Time.Gregorian;
using Toybox.WatchUi;
using Toybox.Sensor;
using Toybox.Math;
using Toybox.SensorLogging;
using Toybox.ActivityRecording;
using Toybox.System;
using Toybox.Attention;
using Toybox.Application;

class ValleFitTrackController {

	enum {
	 INIT, 
	 STARTED_WORKING,
	 PAUSED_WORKING,
	 STARTED_REST,
	 PAUSED_REST, 
	}
	
	var tipo = 1;
	var m_control_series = 0;
	var m_control_ejercicio = 0;
	var choice = false;
	var TIME_REST = 60;

	var status = INIT;	
    var segundos = 0;         //segundos de la actividad en total
	var tiempo = "00:00:00";  //duración desglosada del tiempo que esta durando la actividad.
	
	
	var hr = "000";
	var kal = "0000";
	var set = 0;
	var work = 0;
	var aviso_work = 0;
	var rest;
	var rest_elapsed = 0;
	var lap = 1;
	
	var mLogger;
	var mSession;
	
	var timer_duracion;
	
	var control_series;
	var control_ejercicio;
	var repeticiones_serie;
	var tiempo_descanso;
	var tiempo_trabajo;
	var ejercicio;
	var peso_serie;
	var series;
	
	function initialize() {
	    try {
         
            mSession = ActivityRecording.createSession({:name=>"ValleFitTrack", 
                                                        :sport=>ActivityRecording.SPORT_TRAINING,
                                                        :subsport=>ActivityRecording.SUB_SPORT_CARDIO_TRAINING});
                                                        
            repeticiones_serie = mSession.createField("repeticiones_serie", 0, 
                                                    FitContributor.DATA_TYPE_SINT32, 
                                                   { :mesgType=>FitContributor.MESG_TYPE_RECORD,
                                                     :units=>"rep/ser" });
                                                     
            repeticiones_serie.setData(0);
                                                        
            tiempo_descanso = mSession.createField("tiempo_descanso_serie", 1, 
                                                    FitContributor.DATA_TYPE_SINT32, 
                                                   { :mesgType=>FitContributor.MESG_TYPE_RECORD,
                                                     :units=>"s" });
                                                     
            tiempo_descanso.setData(0);                                                                                   
            
            tiempo_trabajo = mSession.createField("tiempo_trabajo_serie", 2, 
                                                    FitContributor.DATA_TYPE_SINT32, 
                                                   { :mesgType=>FitContributor.MESG_TYPE_RECORD,
                                                     :units=>"s" });                                                                                         
            tiempo_trabajo.setData(0);  
                                                   
            ejercicio = mSession.createField("ejercicio", 3, 
                                                    FitContributor.DATA_TYPE_SINT32, 
                                                   { :mesgType=>FitContributor.MESG_TYPE_RECORD,
                                                     :units=>"ej" });   
            ejercicio.setData(0); 
            
            peso_serie = mSession.createField("peso_serie", 4, 
                                                FitContributor.DATA_TYPE_SINT32, 
                                               { :mesgType=>FitContributor.MESG_TYPE_RECORD,
                                                 :units=>"kg" }); 
            peso_serie.setData(0); 
            series = mSession.createField("series", 5, 
                                            FitContributor.DATA_TYPE_SINT32, 
                                           { :mesgType=>FitContributor.MESG_TYPE_RECORD,
                                             :units=>"ser" });
            series.setData(0); 
            control_series = mSession.createField("control_series", 6, 
                                            FitContributor.DATA_TYPE_SINT32, 
                                           { :mesgType=>FitContributor.MESG_TYPE_RECORD });
            control_series.setData(m_control_series);  
            control_ejercicio = mSession.createField("control_ejercicio", 7, 
                                            FitContributor.DATA_TYPE_SINT32, 
                                           { :mesgType=>FitContributor.MESG_TYPE_RECORD });
            control_ejercicio.setData(m_control_ejercicio);                                         
            
            
        }
        catch(e) {
            System.println(e.getErrorMessage());
        }  
	
	}
	
    function onStart() {  
        status = PAUSED_WORKING;
        try {
            mSession.start();
        }
        catch(e) {
            System.println(e.getErrorMessage());
        }
        
        timer_duracion = new Timer.Timer();
        timer_duracion.start(method(:timer_duracion_callback), 1000, true);
        onOpenEjerciciosDg();
    }
    
    
    function onStartWork(){
          status = STARTED_WORKING;
          aviso_work = Application.getApp().getProperty("work");
          TIME_REST = Application.getApp().getProperty("rest");    
          rest = TIME_REST;
          tiempo_descanso.setData(rest_elapsed);
          control_series.setData(m_control_series);
          m_control_series =  m_control_series + 1;
          rest_elapsed = 0;
          set = set + 1;
          work = 0;
          runVibrate(500);
    }
    
    function onStopWork(){
          status = STARTED_REST;
          tiempo_trabajo.setData(work);
          rest = TIME_REST - 1;
          runVibrate(500);
          choice = true;
          tipo = 2;
          WatchUi.pushView(new NumberPicker("Rep", 100), 
                           new NumberPickerDelegate("Peso", "Rep", 250, repeticiones_serie, peso_serie), WatchUi.SLIDE_IMMEDIATE);       
    }
    
    function onPauseWork(){
          //status = PAUSED_WORKING;
          runVibrate(500);
    }
    
    function onResumeWork(){
          status = STARTED_WORKING;
          runVibrate(500);
    }
    
    function onNextLap(){
        if (set > 0 && status == STARTED_REST  ){
             mSession.addLap();
             m_control_ejercicio =  m_control_ejercicio + 1;
          	 control_ejercicio.setData(m_control_ejercicio);
	         series.setData(set);
	         rest = TIME_REST;
	         lap = lap + 1;
	         set = 0;
	         runVibrate(500);
	         onOpenEjerciciosDg();
         }
    }
   
    function onStop() {
        if ((mSession != null) && mSession.isRecording()) {
           mSession.stop();                                      // stop the session
           mSession = null;                                      // set session control variable to null
       }
       System.exit();
    }
    
    function onCancel(){
       status = PAUSED_WORKING;     
       if ((mSession != null) && mSession.isRecording()) {
            mSession.discard();
            WatchUi.pushView(new MyWatchView(), null, WatchUi.SLIDE_UP );
       }else{
            System.exit();
       }
  
     }
     
    function onOpenEjerciciosDg(){
         choice = true;
         var t = new EjercicioPicker(ejercicio);
         t.onMenu();
    }
    
    function openModPesoDg(){
        WatchUi.pushView(new NumberPicker("Rep", 100), 
                   new NumberPickerDelegate("Peso", "Rep", 250, repeticiones_serie, peso_serie), WatchUi.SLIDE_IMMEDIATE);       
   
    }
     
    
    function calculate_time_track(sec, hora){ 
        if (sec !=null && sec > 0){
        	var h = (sec/3600.0);
	    	var m_totales = (sec/60) % 60;
	    	var m = m_totales > 0 ? m_totales % 3600 : 0;
	    	var s = sec % 60;
	    	if (hora){
	        	return  Lang.format("$1$:$2$:$3$", [h.format("%02d"),m.format("%02d"),s.format("%02d")]);
	        }else{
                return  Lang.format("$1$:$2$", [m.format("%02d"),s.format("%02d")]);
	        }
        }else{
           if (hora){
              return "00:00:00";
           }else{
              return "00:00";
           }
        }
    
      }
    
    
     function timer_duracion_callback() {
          var info = Activity.getActivityInfo();
          if (info != null){
            kal = (info.calories != null) ? info.calories : 0;
            hr = (info.currentHeartRate != null) ? info.currentHeartRate : 0;  
          }
          segundos = segundos + 1;
          if (status == STARTED_WORKING){
             work = work + 1;
             if (aviso_work > 0 && work > aviso_work){
                runVibrate(300);
             }
          }else if (status == STARTED_REST){
          	 if (rest > 0) {
          	 	 rest = rest - 1;
          	 	 if (rest < 7){
          	 	   runVibrate(300);
          	 	 }
          	 }else{
          	 	status = PAUSED_WORKING;
          	 	rest = TIME_REST;
          	 	runVibrate(2000);
          	 }
          }
         
          if (status == PAUSED_WORKING || status == STARTED_REST){
             rest_elapsed = rest_elapsed +1;
          }
          WatchUi.requestUpdate();
     }
    
    
    function runVibrate(s){
      if (Attention has :vibrate) {
            var vibrateData = [
                new Attention.VibeProfile( 100, s ),
              ];

           Attention.vibrate(vibrateData);
        }
    }
    
    function getWork(){
        return calculate_time_track(work, false);
    }
    
    function getSET(){
        return set.format("%02d");
    }
    
    function getTiempo(){
        return calculate_time_track(segundos, true);
    }
    
    function getHora(){
        var today = Gregorian.info(Time.now(), Time.FORMAT_MEDIUM);
        var horaString = Lang.format("$1$:$2$", [today.hour.format("%02d"),today.min.format("%02d"),]);
        return horaString;
    }
    
    function getKAL(){
        return kal;
    }
    
    function getRest(){
        if ((status == PAUSED_WORKING || status == STARTED_REST) &&
                    (TIME_REST != null && rest != null && rest >= TIME_REST)){
            return calculate_time_track(rest_elapsed, false);
        }else{  
           return calculate_time_track(rest, false);
        }
    }
    
    function getHR(){
        return hr;
    }
    
    function getLap(){
        return lap.format("%02d");
    }
    
    function getStatus(){
    	return status;
    }
    

}