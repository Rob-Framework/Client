import serial
from ardu.getch import _Getch
from envReader import getValue

getch = None
ser = None

def sendCommand(cmd):
    ser.write(cmd.enocde())

def runMonitor():
    global getch, ser
    print("Press 'i' for sending data")
    print("Press 'q' to quit")
    port = getValue("ARDUINO_PORT")
    baud = int(getValue("ARDUIONO_BAUD"))

    getch = _Getch()
    ser = serial.Serial(port, baud)
