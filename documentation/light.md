Connect the Light to Frequency Converter - TSL235R. This light sensor is used to identify when it's day or night.
So the connection is too simple the sensor has four cables.




* VCC 3.3V 
* GND 
* OUT




If you identified the pins, connect them to the RPI4:




The OUT pin goes on the 18 gpio on the RPI4 (12 pin on the board), for this pin you can use and another gpio on your board.
After that, connect the GND pin of your sensor to the GND pin on the RPI4 (6 pin on the board) and lastly, the VCC pin of your sensor on the PRI4 (1 pin on the board). When you finish with the connections, you can run the code to test your sensor.