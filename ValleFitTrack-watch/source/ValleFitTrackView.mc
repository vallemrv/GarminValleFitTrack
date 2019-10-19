using Toybox.WatchUi;


class ValleFitTrackView extends WatchUi.View {


	var mLabelHora;
	var mLabelHr;
	var mLabelKal;
	var mLabelSet;
	var mLabelTimer;
	var mLabelWork;
	var mLabelRest;
	var mTracker;
	var mLabelLap;
	
    function initialize(tracker) {
        View.initialize();
        mTracker = tracker;
     }

    // Load your resources here
    function onLayout(dc) {
        setLayout(Rez.Layouts.MainLayout(dc));
        mLabelHora = View.findDrawableById("hora");
        mLabelHr = View.findDrawableById("hr");
        mLabelKal = View.findDrawableById("kal");
    	mLabelTimer = View.findDrawableById("timer");
    	mLabelWork = View.findDrawableById("workout");
    	mLabelSet = View.findDrawableById("set");
    	mLabelRest = View.findDrawableById("rest");
    	mLabelLap = View.findDrawableById("lap");
    }

    // Called when this View is brought to the foreground. Restore
    // the state of this View and prepare it to be shown. This includes
    // loading resources into memory.
    function onShow() {
        if (!mTracker.choice){
	    	var rest = Application.getApp().getProperty("rest");
	        if (rest == null){
		       rest = mTracker.TIME_REST;
		       Application.getApp().setProperty("rest", mTracker.TIME_REST);
		    }
		    
		    var aWork = Application.getApp().getProperty("work");
	        if (aWork == null){
	           aWork = 0;
		       Application.getApp().setProperty("work", aWork);
		    }
		    mTracker.TIME_REST = rest;
		    mTracker.aviso_work = aWork;
		    
	    }else if (mTracker.choice && mTracker.tipo == 1){
	      mTracker.choice = false;
	    }else{
	      mTracker.tipo = mTracker.tipo -1;
	    }
	    
	    
    }
    

    // Update the view
    function onUpdate(dc) {
         mLabelTimer.setText(mTracker.getTiempo().toString()); 
         mLabelHora.setText(mTracker.getHora().toString());
         mLabelHr.setText(mTracker.getHR().toString());
         mLabelKal.setText(mTracker.getKAL().toString());
         mLabelSet.setText(mTracker.getSET().toString());
         mLabelWork.setText(mTracker.getWork().toString());
         mLabelRest.setText(mTracker.getRest().toString());
         mLabelLap.setText(mTracker.getLap().toString());
         
         View.onUpdate(dc); 
         
         if (mTracker.getStatus() == mTracker.INIT) {
         		drawInfo(dc);
         }
           
    }
    
    
    
    function drawInfo(dc){
    
    	dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_GREEN);
        dc.fillCircle(dc.getWidth()/2, dc.getHeight()/2, dc.getWidth()/3);
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_TRANSPARENT);
        dc.drawText(
			        dc.getWidth() / 2,                      // gets the width of the device and divides by 2
			        dc.getHeight() * 0.30,                  // gets the height of the device and divides by 2
			        Graphics.FONT_MEDIUM,                   // sets the font size
			        "Click",  // the String to display
			        Graphics.TEXT_JUSTIFY_CENTER            // sets the justification for the text
                );
                
        dc.drawText(
			        dc.getWidth() / 2,                       // gets the width of the device and divides by 2
			        dc.getHeight() * 0.40,                   // gets the height of the device and divides by 2
			        Graphics.FONT_MEDIUM,                    // sets the font size
			        "aqui para",                              // the String to display
			        Graphics.TEXT_JUSTIFY_CENTER             // sets the justification for the text
                );
                
         dc.drawText(
			        dc.getWidth() / 2,                      // gets the width of the device and divides by 2
			        dc.getHeight() * 0.5,                   // gets the height of the device and divides by 2
			        Graphics.FONT_MEDIUM,                   // sets the font size
			        "iniciar",                         // the String to display
			        Graphics.TEXT_JUSTIFY_CENTER            // sets the justification for the text
                );
                
          
    
        
 
    }
    


    // Called when this View is removed from the screen. Save the
    // state of this View here. This includes freeing resources from
    // memory.
    function onHide() {
    }
    

}
