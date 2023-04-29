from gpiozero import CPUTemperature

cpu = None

def initTemperatureCounter():
    global cpu
    cpu = CPUTemperature()

def getTemperature():
    global cpu
    cpu.temperature
