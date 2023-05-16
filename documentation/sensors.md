# SENSORS

The good think with the RPI4 is you can do what ever you want if you have suitables sensors. So for this project i'll use these sensors:

* [Waveshare Laser Range Sensor (ToF) - UART / CAN Bus](range.md)
* [Light to Frequency Converter - TSL235R](light.md)
* Gravity Triple Axis Accelerometer I2C - LIS2DW12
* Gravity Air Quality Sensor - ENS160
* Waveshare SIM7600E-H 4G HAT (also a sim card)
* Pi camera
* USB camera

The bad part of the RPI4 is you can't connect multi sensors together if you don't have an extendre for the gpios.
So the first think is to connect the Raspberry Pi GPIO Edge Expansion on the HAT (**Note** that you already connected the HAT on the RPI4 and turned it off!). So now you have more gpios to work with. 