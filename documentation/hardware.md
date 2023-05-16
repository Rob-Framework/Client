# ROB FRAMEWORK


## Hardwear Documentation


### The materials you have to buy to build the robotic arm


* Metal Robot Arm Kit for Raspberry Pi (includes everything)
* Raspberry Pi 4
* ZOP Power 11.1V 4500mAh 100C 4S Lipo Battery
* Voltage Regulator LM2576T-ADJG
* Fan for Raspberry Pi
* Raspberry Pi GPIO Edge Expansion


#### These are the materials you have to buy to build the robotic arm.


### How can you build this robotic arm?


* First of all, you have to assemble the robotic hand.


**The kit includes :**


* Metal arm parts x1.
* MG996R Servo x1.
* MG90S Servo x3.
* Servo Driver HAT x1.
* Power adapter standard USB output x1.
* Servo extension wire, 150 mm x 1.
* Srews pack x1.
* Srewdrivers: 2 PCS x 1.


#### Assembly guide
[Hand Doc](hand_doc.pdf)


### Servo Driver HAT


#### User Manual


This servo driver board is an PWM/servo expansion board for the Raspberry Pi. Use
PCA9685 chip, which expands up to 16 channels and supports 12-bit resolution for each
channel. using an I2C interface. This board also integrates a 5V regulator with up to 3A of output.
current, can be powered from the battery through the VIN terminal. It could be used for
Robot applications.


![""](/image/Screenshot_3.png)


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

#### How to enable the Servo Driver HAT on the RPI4
NOTE: You need a monitor to connect to the RPI4 to enable the HAT.


Run this command on the terminal to begin setting.


sudo raspi-config


Choose Interfacing Options->I2C-> yes



