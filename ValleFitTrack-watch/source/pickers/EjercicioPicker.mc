using Toybox.WatchUi;
using Toybox.Graphics;
using Toybox.System;
using Toybox.Application;


class EjercicioPicker{

    hidden var c_field;
    
    function initialize(field) {
       c_field = field;
    }

    function onMenu() {
         // Generate a new Menu with a drawable Title
        var menu = new WatchUi.Menu2({:title=>new DrawableMenuTitle("Works")});
        // Add menu items for demonstrating toggles, checkbox and icon menu items
        menu.addItem(new WatchUi.MenuItem("Pecho", null, "1", null));
        menu.addItem(new WatchUi.MenuItem("Espalda", null, "2", null));
        menu.addItem(new WatchUi.MenuItem("Piernas", null, "3", null));
        menu.addItem(new WatchUi.MenuItem("Brazos", null, "4", null));
        menu.addItem(new WatchUi.MenuItem("Hombros", null, "5", null));
        menu.addItem(new WatchUi.MenuItem("Core", null, "6", null));
        menu.addItem(new WatchUi.MenuItem("Cardio", null, "7", null));          
        WatchUi.pushView(menu, new EjercicioMenuDelegate(c_field), WatchUi.SLIDE_UP );
    }
    
    
    
}

class EjercicioMenuDelegate extends WatchUi.MenuInputDelegate {
    
    hidden var c_field;
    
    function initialize(field) {
       MenuInputDelegate.initialize();
       c_field = field;
     }
    
    function onSelect(item) {
        switch (item.getId().toNumber()){
             case 1:
             case 2:
                Application.getApp().setProperty("peso", 50);
                Application.getApp().setProperty("rep", 10);
               break;
             case 3:
                Application.getApp().setProperty("peso", 100);
                Application.getApp().setProperty("rep", 10);
             break;
             case 4:
             case 5:
                Application.getApp().setProperty("peso", 20);
                Application.getApp().setProperty("rep", 10);
               break;	
             case 6:
                Application.getApp().setProperty("peso", 0);
                Application.getApp().setProperty("rep", 20);
             break;
             case 7:
                Application.getApp().setProperty("peso", 0);
                Application.getApp().setProperty("rep", 1);
             break;	
        
        }
        
        c_field.setData(item.getId().toNumber());
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        return true;
    }

    function onBack() { 
        Application.getApp().setProperty("peso", 0);
        Application.getApp().setProperty("rep", 1);  
        c_field.setData(7);  
        WatchUi.popView(WatchUi.SLIDE_DOWN);
    }
    
    function onNextPage() {
    	Application.getApp().setProperty("peso", 0);
        Application.getApp().setProperty("rep", 1);  
        c_field.setData(7);  
    	WatchUi.popView(WatchUi.SLIDE_DOWN);
    }
    

    

}
