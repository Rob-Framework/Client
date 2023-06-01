from envReader import read, getValue, getBool
from imgClient import initImgClient
from audioSender import initAudioSender
from handlers.location import init as initLocation

def run():
    read()
    initLocation()

    def initArdu():
        if getBool("USE_ARDUINO"):
            from ardu.monitor import runMonitor
            runMonitor()

    def initSensors():
        if getBool("USE_AIR_QUALITY"):
            from handlers.air import setup as airSetup
            airSetup()
        
        if getBool("USE_TEMPERATURE_COUNTER"):
            from drivers.TemperatureCounter import initTemperatureCounter
            initTemperatureCounter()

        if getBool("USE_DAY_NIGHT_SENSOR"):
            from handlers.daynight import init as daynightInit
            daynightInit()
            
        if getBool("USE_HUMIDITY"):
            from handlers.humidity import init as initHumidity
            initHumidity()

    initArdu()
    initSensors()

    initImgClient()

def Clean():
    if bool(getValue("USE_LIGHT")):
        from handlers.light import Clean as lightClean
        lightClean()