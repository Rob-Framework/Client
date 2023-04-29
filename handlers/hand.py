from drivers.PCA9685Driver import PCA9685

pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

def openCrab(servo):
    pwm.setServoPulse(2, servo)

def closeCrab(servo):
    pwm.setServoPulse(2, servo)
 
def moveForward(servo):
    pwm.setPWM(0,0,1024)
    pwm.setServoPulse(0, servo)
 
def moveBackward(servo):
    pwm.setPWM(0,0,1024)
    pwm.setServoPulse(0, servo)
 
def rotateLeft(servo):
    pwm.setServoPulse(3, servo)
 
def rotateRight(servo):
    pwm.setServoPulse(3, servo)
 
def moveDown(servo):
    pwm.setPWM(1,0,1024)
    pwm.setServoPulse(1, servo)
 
def moveUp( servo):
    pwm.setPWM(1,1024,4095)
    pwm.setServoPulse(1, servo)

if __name__ == '__main__':
  while True:
    input1 = input("Action: ")

    if (input1 == "1"):
        openCrab(2500)
    if (input1 == "2"):
        closeCrab(500)
    if (input1 == "3"):
        moveForward(1000)
    if (input1 == "4"):
        moveBackward(500)
    if (input1 == "5"):
        rotateLeft(2500)
    if (input1 == "6"):
        rotateRight(500)
    if (input1 == "7"):
        moveDown(2500)
    if (input1 == "8"):
        moveUp(500)
    if (input1 == "q"):
        openCrab(1500)
    if (input1 == "w"):
        closeCrab(1000)
    if (input1 == "e"):
        moveForward(1000)
    if (input1 == "r"):
        moveBackward(1000)
    if (input1 == "t"):
        rotateLeft(1500)
    if (input1 == "y"):
        rotateRight(1000)
    if (input1 == "u"):
         moveDown(1500)
    if (input1 == "i"):
        moveUp(1000)
        

