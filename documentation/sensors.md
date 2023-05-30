# SENSORS

The Raspberry Pi 4 (RPI4) offers great flexibility for various projects, thanks to its compatibility with a wide range of sensors. For this particular project, the following sensors will be used:

* [Waveshare Laser Range Sensor (ToF) - UART / CAN Bus](range.md)
* [Light to Frequency Converter - TSL235R](light.md)
* [Gravity Triple Axis Accelerometer I2C - LIS2DW12](accelerometer.md)
* [Gravity Air Quality Sensor - ENS160](airquality.md)
* [Temperature & Humidity Sensor - DHT11 ESP-01/01S](humidity.md)
* [Waveshare SIM7600E-H 4G HAT](sim.md)
* Pi camera
* USB camera

However, one limitation of the RPI4 is that it has a limited number of GPIO pins available for sensor connections. To overcome this limitation, the Raspberry Pi GPIO Edge Expansion HAT can be used. It provides additional GPIO pins, enabling the connection of multiple sensors simultaneously. Please note that you should connect the HAT to the RPI4 while it is turned off. This expansion will give you more GPIOs to work with, expanding the capabilities of your Raspberry Pi.

By incorporating these sensors and utilizing the GPIO expansion, you can enhance the functionality and versatility of your Raspberry Pi 4 project.