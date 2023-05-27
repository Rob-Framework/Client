from envReader import getBool
import safeguard

def handleCommand(cmdObj):
    cmd = cmdObj["command"]

    if cmd == "forward" or cmd == "backward" or cmd == "left" or cmd == "right" or cmd == "stop" or cmd == "break" or cmd == "slow_stop":
        if getBool("USE_ARDUINO"):
            from ardu.monitor import sendCommand
            safeguard.newCommand(cmd)
            sendCommand(cmd)
    elif cmd == "move_hand":
        if getBool("USE_HAND"):
            import handlers.hand as hand

            movement = cmdObj["movement"]
            servo = int(cmdObj["servo"])

            if movement == "open_crab":
                hand.openCrab(servo)
            elif movement == "close_crab":
                hand.closeCrab(servo)
            elif movement == "forward":
                hand.moveForward(servo)
            elif movement == "backward":
                hand.moveBackward(servo)
            elif movement == "left":
                hand.rotateLeft(servo)
            elif movement == "right":
                hand.rotateRight(servo)
            elif movement == "up":
                hand.moveUp(servo)
            elif movement == "down":
                hand.moveDown(servo)