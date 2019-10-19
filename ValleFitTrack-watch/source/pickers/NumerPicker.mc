using Toybox.Application;
using Toybox.Graphics;
using Toybox.System;
using Toybox.WatchUi;

class NumberPicker extends WatchUi.Picker {

    function initialize(title_menu, num_max) {
    
        var title = new WatchUi.Text({:text=>title_menu, 
                                      :locX=>WatchUi.LAYOUT_HALIGN_CENTER, 
                                      :locY=>WatchUi.LAYOUT_VALIGN_BOTTOM,
                                      :color=>Graphics.COLOR_WHITE});
        
        var value = Application.getApp().getProperty(title_menu.toLower());
        Picker.initialize({:title=>title, 
                           :pattern=>[new NumberFactory(0, num_max, 1, {})], 
                           :defaults=>[value]});
    }
    
    

    function onUpdate(dc) {
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        Picker.onUpdate(dc);
    }
       
}


class NumberPickerDelegate extends WatchUi.PickerDelegate {
	 
	var c_title;
    var c_max;
    var c_field;
    var c_field2;
    var c_title2;
	
    function initialize(title, title2, max, field, field2) {
        PickerDelegate.initialize();
        c_title = title;
        c_title2 = title2;
        c_max = max;
        c_field = field;
        c_field2 = field2;
    }

    function onCancel() { 
       WatchUi.popView(WatchUi.SLIDE_LEFT);
        if (c_title !=null){
	        WatchUi.pushView(new NumberPicker(c_title, c_max), 
	                         new NumberPickerDelegate(null, c_title, null, c_field2, null), WatchUi.SLIDE_UP); 
        }      
    }

    function onAccept(values) {
         var value = values[0];
         c_field.setData(value + 0);
         Application.getApp().setProperty(c_title2.toLower(), value);
    	 WatchUi.popView(WatchUi.SLIDE_IMMEDIATE);
         if (c_title !=null){ 
	        WatchUi.pushView(new NumberPicker(c_title, c_max), 
	                         new NumberPickerDelegate(null, c_title, null, c_field2, null), WatchUi.SLIDE_IMMEDIATE); 
         }  
    }
    
    

}
