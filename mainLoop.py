from envReader import getBool
from audioSender import audioSenderLoop

def Loop():
    if getBool("USE_AIR"):
        from handlers.air import Run as airRun
        airRun()
    
    if getBool("USE_LIGHT"):
        from handlers.light import Run as lightRun
        lightRun()

    if getBool("USE_ACCELEROMETER"):
        from handlers.accelerometer import Run as accelerateRun
        accelerateRun()

    if getBool("USE_ORIENTATION"):
        from handlers.orientation import Run as orientationRun
        orientationRun()
    
    audioSenderLoop()