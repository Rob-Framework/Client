# ROB FRAMEWORK


## Hardware Documentation


### The materials you have to buy to build the robotic arm


* Metal Robot Arm Kit for Raspberry Pi (includes everything)
* Raspberry Pi 4
* ZOP Power 11.1V 4500mAh 100C 4S Lipo Battery
* Power Bank 20.000 mAh
* Fan
* Raspberry Pi GPIO Edge Expansion

### [SENSORS](sensors.md)

#### These are the materials you have to buy to build the robotic arm.


### How can you build this robotic arm?


* First of all, you have to assemble the robotic hand.


**The kit includes :**


* Metal arm parts x1
* MG996R Servo x1
* MG90S Servo x3
* Servo Driver HAT x1
* Power adapter EU standard USB output x1.
* Servo extension wire 150mm x1
* Screws pack x1
* Screwdrivers 2PCS x1


#### Assemblance guide
[Hand Doc](hand_doc.pdf)


### Servo Driver HAT


#### User Manual


This servo driver board is an PWM/servo expansion board for the Raspberry Pi. Use
PCA9685 chip, which expands up to 16 channels and supports 12-bit resolution for each
channel, using an I2C interface. This board also integrates a 5V regulator with up to 3A of output.
current, can be powered from the battery through the VIN terminal. It could be used for
Robot applications.


![""](/documentation/images/hat.png)

#### Characteristic


 * Power supply: 6V–12V
 * Servo voltage: 5 V
 * Logic voltage: 3.3V
 * Driver: PCA9685
 * Control interface: I2C
 * Dimension: 65mm x 36mm
 * Mounting hole size: 3.0mm


Connect the HAT to the Raspberry Pi 4, and then connect the servo motor cables to the HAT by color.
(Note: don't turn on the Raspberry Pi 4 if you don't finish with cables!)

So after that, you have to give power to the Raspberry Pi 4. To do that, you have to connect the power bank to the power supply of the Raspberry Pi, and with this simple way, you powered your Raspberry Pi!


#### How to enable the Servo Driver HAT on the RPI4
NOTE: You need a monitor to connect to the RPI4 to enable the HAT.


Run this command on the terminal to begin setting.


sudo raspi-config


Choose Interfacing Options->I2C-> yes