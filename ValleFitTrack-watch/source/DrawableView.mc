//
// Copyright 2015-2016 by Garmin Ltd. or its subsidiaries.
// Subject to Garmin SDK License Agreement and Wearables
// Application Developer Agreement.
//

using Toybox.WatchUi;
using Toybox.Graphics;
using Toybox.System;
using Toybox.Lang;
using Toybox.Time.Gregorian;
using Toybox.Timer;

class MyWatchView extends WatchUi.View {

    var train;
    var backdrop;
    var cloud;
    

    // Constructor
    function initialize() {
        View.initialize();
        train = new Rez.Drawables.train();
        backdrop = new Rez.Drawables.backdrop();
        cloud = new WatchUi.Bitmap({:rezId=>Rez.Drawables.cloud,:locX=>10,:locY=>30});
    }

    // Load your resources here
    function onLayout(dc) {
        WatchUi.animate( cloud, :locX, WatchUi.ANIM_TYPE_LINEAR, 10, dc.getWidth() + 50, 10, null );
    }

    function onShow() {
        var timer_duracion = new Timer.Timer();
        timer_duracion.start(method(:timer_callback), 5000, false);
    }
    
    function timer_callback(){
        System.exit();
    }

    // Update the view
    function onUpdate(dc) {
        dc.setColor(Graphics.COLOR_BLUE, Graphics.COLOR_BLACK);
        dc.fillRectangle(0, 0, dc.getWidth(), dc.getHeight());
        backdrop.draw(dc);
        train.draw(dc);
        cloud.draw(dc);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT); 
        dc.drawText(dc.getWidth() * 0.50, dc.getHeight() * 0.2, Graphics.FONT_LARGE, "Saliendo....", Graphics.TEXT_JUSTIFY_CENTER);
    }

}
