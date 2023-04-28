import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set GPIO pin for TSL235R sensor input
gpio_pin = 18

# Set up GPIO input pin
GPIO.setup(gpio_pin, GPIO.IN)

# Wait for sensor to settle
time.sleep(2)

while True:
    # Set up variables for frequency and light intensity
    frequency = 0
    light_intensity = 0

    # Read frequency output from sensor for 5 seconds
    start_time = time.time()
    while (time.time() - start_time) < 5:
        if GPIO.input(gpio_pin):
            frequency += 1

    # Calculate light intensity as a percentage
    light_intensity = (frequency / 5000) * 100

    # Print light intensity value
    print("Light intensity: {:.2f}%".format(light_intensity))

# Clean up GPIO
GPIO.cleanup()