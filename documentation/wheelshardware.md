# ROB FRAMEWORK: Hardware Documentation

#### To build the wheels of your robot, you will need the following materials:

* Arduino Mega
* DC Gear Motor TT – 125 RPM x4
* L298N Dual H Bridge Stepper Motor Driver Board
* ZOP Power 11.1V 4500mAh 100C 4S Lipo Battery
* Custom-made plastic case for the body
* Jumper Wires Standard 7″ M/M
* Hobbywing 35x35x10mm Cooling Fan
* USB fan (for Arduino)

**Building the Robot**

1. Start by deciding on the material for the robot body. In this case, plastic is chosen. Determine the shape of the robot as well.

2. Once the body is complete, connect the Arduino with the motor driver board (L298N), motors, and the battery.

3. The connection between the motor driver board (L298N) and Arduino is straightforward. The driver board has six pins:

* ENA
* ENB
* IN1
* IN2
* IN3
* IN4
4. Remove the two jumpers on the driver board (L298N). Connect the left pin of the driver board to the 9-pin PWM of the Arduino, and the right pin to the 10-pin PWM of the Arduino. The connection for the other pins is as follows:

* IN1: PWM pin 2 of the Arduino
* IN2: PWM pin 3 of the Arduino
* IN3: PWM pin 4 of the Arduino
* IN4: PWM pin 5 of the Arduino
This completes the connection between the driver board and the Arduino Mega.

5. Connect the motors to the driver board (L298N). Each motor has a red power cable and a black ground cable.

* OUT1: Connect two red cables to two motors.
* OUT2: Connect two black cables to two motors.
* OUT3: Connect two black cables to the other two motors.
* OUT4: Connect two red cables of the remaining two motors.


**Note: Connect the motors in pairs: front left motor with back left motor (OUT1 and OUT2), and front right motor with back right motor (OUT3 and OUT4).**

1. Power all the systems by using a ZOP Power 11.1V 4500mAh 100C 4S Lipo Battery. Identify the wire clamps on the driver board (L298N) that will connect the battery:

* Left wire clamp: 12V
* Middle wire clamp: GND
* Right wire clamp: 5V


Connect the positive (+) cable (red) of the battery to the 12V wire clamp of the driver board (L298N), and connect the negative (-) cable (black) of the battery to the GND wire clamp of the driver board. To power the Arduino, connect the GND pin on the Arduino board to the middle wire clamp of the driver board using the negative (-) cable (black) of the battery.

**Note: Connect the positive (+) cable (red) of the battery to the driver board (L298N) as the last step to prevent any damage to the boards.**

Congratulations! Your robot is now ready to be powered on and brought to life.

To control the robot, run your code and test its functionality.

Remember, safety precautions should be taken while working with electronics and power sources.