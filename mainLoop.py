from envReader import getBool
from audioSender import audioSenderLoop
from handlers.location import getLongLat
from tcpServer import getTCPServer as getServer
from handlers.cpu import getCPUUsage

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

    if (getBool("USE_DISTANCE")):
        from handlers.distance import Run as distanceRun
        distanceRun()
    
    if getBool("USE_LIGHT"):
        from handlers.light import Run as lightRun
        lightRun()

    if getBool("USE_ACCELEROMETER"):
        from handlers.accelerometer import Run as accelerateRun
        accelerateRun()

    if getBool("USE_ORIENTATION"):
        from handlers.orientation import Run as orientationRun
        orientationRun()
    
    if getBool("USE_DAY_NIGHT_SENSOR"):
        from handlers.daynight import loop as daynightRun
        mode = daynightRun()
        
        data = {
            "mode": mode
        }

        getServer().sendSensorData("daynight", data)
        
    if getBool("USE_HUMIDITY"):
        from handlers.humidity import loop as humitidyRun
        humitidyRun()

    audioSenderLoop()
    sendLongLat()
    getCPUUsage()