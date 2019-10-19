using Toybox.Application;
using Toybox.WatchUi;

class ValleFitTrackApp extends Application.AppBase {

    hidden var controller;

    function initialize() {
        AppBase.initialize();
    }

    // onStart() is called on application start up
    function onStart(state) {
    }

    // onStop() is called when your application is exiting
    function onStop(state) {
         return false;
    }

    // Return the initial view of your application here
    function getInitialView() {
        controller = new ValleFitTrackController();
        return [ new ValleFitTrackView(controller), new ValleFitTrackDelegate(controller) ];
    }

}
