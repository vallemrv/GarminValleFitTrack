using Toybox.WatchUi;
using Toybox.Graphics;
using Toybox.System;
using Toybox.Application;


class ValleFitTrackDelegate extends WatchUi.BehaviorDelegate {

    hidden var mTracker;

    function initialize(tracker) {
       BehaviorDelegate.initialize();
       mTracker = tracker;
    }

    function onMenu() {
         // Generate a new Menu with a drawable Title
        var menu = new WatchUi.Menu2({:title=>new DrawableMenuTitle("Menu")});
        // Add menu items for demonstrating toggles, checkbox and icon menu items
        menu.addItem(new WatchUi.MenuItem("Ejercicio", null, "ejer", null));
        menu.addItem(new WatchUi.MenuItem("Modificar", "ult. serie", "pes", null));
        menu.addItem(new WatchUi.MenuItem("Set rest", null, "rest", null));
        menu.addItem(new WatchUi.MenuItem("Aviso work", null, "work", null));
        menu.addItem(new WatchUi.MenuItem("Save", "Exit", "save", null));
        menu.addItem(new WatchUi.MenuItem("Cancel", "Exit", "cancel", null));
        WatchUi.pushView(menu, new ValleFitTrackMenuDelegate(mTracker), WatchUi.SLIDE_UP );
        return true;
    }

    function onSelect() {
      	if (mTracker.getStatus() == mTracker.INIT){
      	    mTracker.onStart();
      	}else if (mTracker.getStatus() == mTracker.PAUSED_WORKING){
      	    mTracker.onStartWork();
      	}else if (mTracker.getStatus() == mTracker.STARTED_WORKING){
      	    mTracker.onStopWork();
      	}
        return true;
    }


    function onSwipe(evt) {
       mTracker.onNextLap();
       return true;
    }

    function onRelease( evt ){
       return true;
    }

   	function onKey(evt){
   	   return true;
   	}

    function onKeyPressed(evt) {
       return true;
    }

}


// This is the custom drawable we will use for our main menu title
class DrawableMenuTitle extends WatchUi.Drawable {
    var mIsTitleSelected = false;
    var c_title = "Menu";

    function initialize(title) {
        Drawable.initialize({});
        c_title = title;
    }

    function setSelected(isTitleSelected) {
        mIsTitleSelected = isTitleSelected;
    }

    // Draw the application icon and main menu title
    function draw(dc) {
        var spacing = 2;
        var appIcon = WatchUi.loadResource(Rez.Drawables.LauncherIcon);
        var bitmapWidth = appIcon.getWidth();
        var labelWidth = dc.getTextWidthInPixels(c_title, Graphics.FONT_MEDIUM);

        var bitmapX = (dc.getWidth() - (bitmapWidth + spacing + labelWidth)) / 2;
        var bitmapY = (dc.getHeight() - appIcon.getHeight()) / 2;
        var labelX = bitmapX + bitmapWidth + spacing;
        var labelY = dc.getHeight() / 2;

        var bkColor = mIsTitleSelected ? Graphics.COLOR_BLUE : Graphics.COLOR_BLACK;
        dc.setColor(bkColor, bkColor);
        dc.clear();

        dc.drawBitmap(bitmapX, bitmapY, appIcon);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(labelX, labelY, Graphics.FONT_MEDIUM, "Menu", Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}
