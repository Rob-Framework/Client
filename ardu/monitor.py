import serial
from ardu.getch import _Getch
from envReader import getValue

getch = None
ser = None

def sendCommand(cmd):
    ser.write(cmd.encode())

def runMonitor():
    global getch, ser
    port = getValue("ARDUINO_PORT")
    baud = int(getValue("ARDUIONO_BAUD"))

    getch = _Getch()
    ser = serial.Serial(port, baud)
