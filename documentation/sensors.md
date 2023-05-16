# SENSORS


The good thing about the RPI4 is that you can do whatever you want if you have suitable sensors. So for this project, I'll use these sensors:


* [Waveshare Laser Range Sensor (ToF) - UART / CAN Bus](range.md)
* [Light to Frequency Converter - TSL235R](light.md)
* [Gravity Triple Axis Accelerometer I2C - LIS2DW12](accelerometer.md)
* [Gravity Air Quality Sensor - ENS160](airquality.md)
* [Temperature & Humidity Sensor - DHT11 ESP-01/01S](humidity.md)
* [Waveshare SIM7600E-H 4G HAT](sim.md)
* Pi camera
* USB camera


The bad part of the RPI4 is that you can't connect multiple sensors together if you don't have an extender for the gpios.
So the first thing to do is connect the Raspberry Pi GPIO Edge Expansion on the HAT (**Note** that you already connected the HAT on the RPI4 and turned it off!). So now you have more gpios to work with.