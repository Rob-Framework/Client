Connect the Waveshare Laser Range Sensor (ToF) - UART / CAN Bus. This proximity sensor is used to locate obstacles on the road ahead of the robot.
So the connection is too simple the sensor has four cables.


* VCC 5V (red cable)
* GND (black cable)
* RX (blue cable)
* TX (yellow cable)

Raspberry Pi Serial Port Setting
Due to the serial port of the Raspberry Pi being for terminal debugging by default, you need to modify the Raspberry Pi setting when using the serial port. Please execute the following demand to enter the Raspberry Pi setting:

sudo raspi-config
Choose Interfacing Options ->Serial ->no -> yes and close the serial debugging function.

sudo reboot

If you identified the cables, connect them to the RPI4:


The TX cable goes on the RX gpio on the RPI4 (10 pin on the board) and the RX cable goes on the TX gpio on the RPI4 (8 pin on the board).
After that, connect the GND cable to the GND pin on the RPI4 (6 pin on the board) and lastly, the VCC cable on the PRI4 (2 or 4 pin on the board). When you finish with the connections, you can run the code to test your sensor.