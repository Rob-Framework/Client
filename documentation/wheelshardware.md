# ROB FRAMEWORK


## Hardwear Documentation


### The materials you have to buy to build the wheels of your robot


* Arduino Mega
* DC Gear Motor TT – 125 RPM X4
* L298N Dual H Bridge Stepper Motor Driver Board
* ZOP Power 11.1V 4500mAh 100C 4S Lipo Battery
* A plastic case for the body (custom-made)
* Jumper Wires Standard 7″ M/M
* Hobbywing 35x35x10mm Cooling Fan
* USB fan (for Arduino)


#### These are the materials you have to buy to build the wheels of your robot.


### How can you build this.


First, you have to decide what material you are going to use to build the body of your robot. I chose plastic. Also, you have to decide on the shape of your robot.


So when you finish with the body, you connect the Arduino with the motor driver board (L298N), your motors and the battery.


It's a simple connection if you identify the pins on the Arduino.
So the first connection will be the motor driver motor (L298N) and Arduino. The driver board (L298N) has 6 pins:


* ENA
* ENB
* IN1
* IN2
* IN3
* IN4


First, you have to remove the 2 jumpers on the driver board (LN298N). After that, connect the left pin on the driver board (LN298N) to the 9-pin PWM of the Arduino. Do the same thing with the right pin of the driver board (LN298N) to the 10-pin PWM of the Arduino.For the other pins of your driver board (L298N) the connection is:


* IN1 pin of your driver board (L298N) goes on PWM pin 2 of the Arduino.
* IN2 pin of your driver board (L298N) goes on PWM pin 3 of the Arduino.
* IN3 pin of your driver board (L298N) goes on PWM pin 4 of the Arduino.
* IN4 pin of your driver board (L298N) goes on PWM pin 5 of the Arduino.


and with a simple way you connected the driver board with the Arduino Mega!


After that, you have to connect your motors to the driver board (L298N).


So first, you have to identify the wire clamps on your driver board (L298N) for the motors. These wire clamps are left and right of your driver board (L298N) in pairs. On the left side of your driver board (L298N) is the wire clamp with 2 screws, one is the OUT1 and the other is the OUT2, respectively is from the right side of your driver board (L298N), you have OUT3 and OUT4.


For this project, we will use 4 DC Gear Motor TT – 125 RPM. Each motor has two cables:


* Red cable which is the power
* Black cable which is the GND


When you identify the cables, you have to connect them to your driver board (L298N). We will connect to the wire clamps of your driver board (L298N) two cables on each OUT wire clamp:


* OUT1 connect two red cables to two motors.
* OUT2 connects two black cables to two motors.
* OUT3 connect two black cables to the other two motors.
* OUT4 connect two red cables of two motors you have left.


**Note: You have to connect the four motors on your driver board (L298N) in pair. For example, the front left motor goes with the back left motor (OUT1 and OUT2) and the front right motor goes with the back right motor (OUT3 and OUT4)!!!**


#### So when you finish with connections, you have to power all of your systems and give life to your robot!


For the power of the robot, I used a ZOP Power 11.1V 4500mAh 100C 4S Lipo Battery (you can change this battery and put in a battery with more mAH). First, you have to identify the wire clamps on your driver board (L298N) which will connect the battery. On the front side of your driver board (L298N) there is a triple wire clamp:


* Left wire clamp is for 12V.
* Middle wire clamp is GND.
* Rifgr wire clamp is for 5V.


With this battery, you have to power your motors and your Arduino. So you have to connect the positive (+) cable (red) of your battery on the 12V wire clamp of your driver board (L298N) and then connect the negative (-) cable (black) of your battery on the GND wire clamp of your driver board (L298N). For now, you have power only for the driver board (L298N) and the motors. So to power your Arduino, the only thing you have to do is locate the GND pin on your Arduino, which is on the power pins on your board (Arduino) and connect it with the middle wire clamp of your driver board (L298N) with the negative (-) cable (black) of your battery.


**Note: To be sure not to cause damage to your boards, it will be good to connect the positive (+) cable (red) of your battery last on the driver board (L298N)!**


#### And there you have it!!!


The only thing you have to do is run your code and test your robot!

