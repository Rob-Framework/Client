from envReader import getBool
from audioSender import audioSenderLoop
from handlers.location import getLongLat
from tcpServer import getTCPServer as getServer

def sendLongLat():
    longlat = getLongLat()
    long = longlat[0]
    lat = longlat[1]
    
    data = {
        "long": long,
        "lat": lat
    }
    getServer().sendSensorData("location", data)

def Loop():
    if getBool("USE_AIR_QUALITY"):
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
    sendLongLat()