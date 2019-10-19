using Toybox.Application;
using Toybox.Graphics;
using Toybox.System;
using Toybox.WatchUi;

const NUMBER_FORMAT = "%02d";

class TimePicker extends WatchUi.Picker {

    function initialize(name) {

        var title = new WatchUi.Text({:text=>"Tiempo", 
                                      :locX=>WatchUi.LAYOUT_HALIGN_CENTER, 
                                      :locY=>WatchUi.LAYOUT_VALIGN_BOTTOM,
                                      :color=>Graphics.COLOR_WHITE});
        
        var value = Application.getApp().getProperty(name);
        Picker.initialize({:title=>title, 
                           :pattern=>[new NumberFactory(0, 60*5, 1, {:format=>NUMBER_FORMAT})], 
                           :defaults=>[value]});
    }

    function onUpdate(dc) {
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        Picker.onUpdate(dc);
    }
       
}

class TimePickerDelegate extends WatchUi.PickerDelegate {
	var propertie_name = "rest";
	
	
    function initialize(name) {
        PickerDelegate.initialize();
        propertie_name = name;
    }

    function onCancel() {
        WatchUi.popView(WatchUi.SLIDE_IMMEDIATE);
    }

    function onAccept(values) {
        Application.getApp().setProperty(propertie_name, values[0]);
        WatchUi.popView(WatchUi.SLIDE_IMMEDIATE);
    }

}
