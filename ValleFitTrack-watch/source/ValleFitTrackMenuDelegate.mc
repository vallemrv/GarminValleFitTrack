using Toybox.WatchUi;
using Toybox.System;
using Toybox.Application;


class ValleFitTrackMenuDelegate extends WatchUi.MenuInputDelegate {


	var mTracker;
	
    function initialize(tracker) {
        MenuInputDelegate.initialize();
        mTracker = tracker;
    }

    function onSelect(item) {
    	 if( item.getId().equals("rest") ) {
           WatchUi.pushView(new TimePicker("rest"), new TimePickerDelegate("rest"), WatchUi.SLIDE_IMMEDIATE);
        }else if( item.getId().equals("work") ) {
           WatchUi.pushView(new TimePicker("work"), new TimePickerDelegate("work"), WatchUi.SLIDE_IMMEDIATE);
        }else if( item.getId().equals("save") ) {
        	mTracker.onStop();    
        }else if( item.getId().equals("cancel") ) {
         	mTracker.onCancel();
        }else if(item.getId().equals("ejer") ) {
            WatchUi.popView(WatchUi.SLIDE_DOWN);
         	mTracker.onOpenEjerciciosDg();
        }else if(item.getId().equals("pes")) {
            WatchUi.popView(WatchUi.SLIDE_DOWN);
         	mTracker.openModPesoDg();
        }
      return true;   
    }
    
    function onBack() {
        WatchUi.popView(WatchUi.SLIDE_DOWN);
    }
    
    function onNextPage() {
    	WatchUi.popView(WatchUi.SLIDE_DOWN);
    }

}

