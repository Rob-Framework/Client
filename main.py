from envReader import read, getValue, getBool
from imgClient import initImgClient
from audioSender import initAudioSender

read()

def initArdu():
    if getBool("USE_ARDUINO"):
        from ardu.monitor import runMonitor
        runMonitor()

def initSensors():
    if bool(getValue("USE_AIR")):
        from handlers.air import setup as airSetup
        airSetup()

initArdu()
initSensors()

initAudioSender()
initImgClient()

def Clean():
    if bool(getValue("USE_LIGHT")):
        from handlers.light import Clean as lightClean
        lightClean()