Connect the Gravity Air Quality Sensor - ENS160. This sensor is to detect the quality of the air.
So the connection is too simple, the sensor has four cables.


* Vdd 3.3v (red cable)
* GND (black cable)
* SDA (green cable)
* SCL (blue cable)


If you identified the cables, connect them to the RPI4:


First, the SDA cable of your sensor goes on the SDA pin of your board (gpio 2 or pin 3), the SCL cable of your sensor goes on the SCL pin of your board (gpio 3 or pin 5), GND cable goes on the GND pin of your board (9 pin or 6pin or 25, there is more) and last the Vdd cable goes on the 3.3v pin of your board (1 pin). When you finish with the connections, you can run the code and test your sensor.