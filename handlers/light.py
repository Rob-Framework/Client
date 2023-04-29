import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gpio_pin = 18

GPIO.setup(gpio_pin, GPIO.IN)

time.sleep(2)

def Run():
    frequency = 0
    light_intensity = 0

    start_time = time.time()
    while (time.time() - start_time) < 5:
        if GPIO.input(gpio_pin):
            frequency += 1

    light_intensity = (frequency / 5000) * 100

    print("Light intensity: {:.2f}%".format(light_intensity))

def Clean():
    GPIO.cleanup()