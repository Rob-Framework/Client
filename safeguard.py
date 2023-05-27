import commandHandler

last_command = ""
last_distance = -1

min_distance_to_stop = 10

def newCommand(command):
    global last_command
    last_command = command

def getLastCommand():
    global last_command
    return last_command

def isCommand(command):
    global last_command
    return last_command == command

def isNotCommand(command):
    global last_command
    return last_command != command

def getNewDistanceInfo(distance):
    global last_distance
    last_distance = distance
    checkDistanceSafety()

def checkDistanceSafety():
    global last_distance
    if last_distance > min_distance_to_stop:
        newCommand("stop")
        commandHandler.handleCommand({"command": "stop"})
