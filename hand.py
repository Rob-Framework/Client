from main import PCA9685

pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

def openCrab(pwm,servo):
    pwm.setServoPulse(2, servo)

 
def closeCrab(pwm,servo):
    pwm.setServoPulse(2, servo)
 
def moveForward(pwm,servo):
    pwm.setPWM(0,0,1024)
    pwm.setServoPulse(0, servo)
 
def moveBackward(pwm,servo):
    pwm.setPWM(0,0,1024)
    pwm.setServoPulse(0, servo)
 
def rotateLeft(pwm,servo):
    pwm.setServoPulse(3, servo)
 
def rotateRight(pwm,servo):
    pwm.setServoPulse(3, servo)
 
def moveDown(pwm,servo):
    pwm.setPWM(1,0,1024)
    pwm.setServoPulse(1, servo)
 
def moveUp(pwm, servo):
    pwm.setPWM(1,1024,4095)
    pwm.setServoPulse(1, servo)

if __name__ == '__main__':
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(50)

  while True:
    input1 = input("Action: ")

    if (input1 == "1"):
        openCrab(pwm,2500)
    if (input1 == "2"):
        closeCrab(pwm,500)
    if (input1 == "3"):
        moveForward(pwm,1000)
    if (input1 == "4"):
        moveBackward(pwm,500)
    if (input1 == "5"):
        rotateLeft(pwm,2500)
    if (input1 == "6"):
        rotateRight(pwm,500)
    if (input1 == "7"):
        moveDown(pwm,2500)
    if (input1 == "8"):
        moveUp(pwm,500)
    if (input1 == "q"):
        openCrab(pwm,1500)
    if (input1 == "w"):
        closeCrab(pwm,1000)
    if (input1 == "e"):
        moveForward(pwm,1000)
    if (input1 == "r"):
        moveBackward(pwm,1000)
    if (input1 == "t"):
        rotateLeft(pwm,1500)
    if (input1 == "y"):
        rotateRight(pwm,1000)
    if (input1 == "u"):
         moveDown(pwm,1500)
    if (input1 == "i"):
        moveUp(pwm,1000)
        

