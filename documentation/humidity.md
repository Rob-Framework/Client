Connect the Temperature and Humidity Sensor - DHT11 ESP-01/01S. This sensor is used to identify the temperature and humidity of the environment in which your robot moves.
To make this connection, first of all, you have to identify the pins of your sensor:


* Vcc 3.3v (the left pin of the front of your sensor)
* OUT (next to the VCC pin)
* NC (We don't need this.)
* GND


This sensor doesn't have cables, so you have to solder cables with suitable ones to make sure your connection will be okay.
When you finish with the connection of your cables on the sensor, connect the OUT cable of your sensor to a gpio on the RPI4. You can choose the gpio pin that you want to use, but for this example, we will use the gpio 17. After that, connect the GND cable to the GND pin of your board (39 pin or 34 pin or 20 pin), and then connect the VCC cable to the VCC pin of your board (pins 1, 3.3v).
When you finish with the connections, you can run the code and test your sensor.