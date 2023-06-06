import RPi.GPIO as GPIO
import time

servo1_pin = 17
servo2_pin = 18


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(servo1_pin, GPIO.OUT)
GPIO.setup(servo2_pin, GPIO.OUT)

servo1_pwm = GPIO.PWM(servo1_pin, 50)
servo2_pwm = GPIO.PWM(servo2_pin, 50)


servo1_pwm.start(0)
servo2_pwm.start(0)

def set_servo_angle(pwm, angle):
    duty = angle / 18+2
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.3)

try:

    while True:
        angle1 = int(input("Enter angle for servo 1 (0-180): "))
        angle2 = int(input("Enter angle for servo 2 (0-180): "))
        
        set_servo_angle(servo1_pwm, angle1)
        set_servo_angle(servo2_pwm, angle2) 
            
except KeyboardInterrupt:
    servo1_pwm.stop()
    servo2_pem.stop()
    GPIO.cleanup()