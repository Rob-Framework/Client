Connect the Waveshare SIM7600E-H 4G HAT. This module is used to have an internet connection on your robot and also make calls or send messages through the Raspberry Pi 4.
So the connection is too simple.


When the power is off, connect the SIM card to your module (on the back side of the module), connect the USB cable, the GPS (on the front side of the module), and lastly, the LTE antenna (also on the front side of the module). It's optional if you want to connect headphones to your module or a TF card.


* In the new version, PWR and 3V3 are short-circuited by default, so the HAT turns on automatically after connecting to the power supply.
* If you need to use the PWRKEY button to turn on/off the HAT, please remove the jumper cap between PWR and 3V3.
* If you want to use the Raspberry Pi to turn on/off, please set the jumper cap between PWR and D6.
* Also, if you need to control the flight mode through the Raspberry Pi pins, set the jumper cap between Flight and D4.


**NOTE**:There are 3 jumpers with your module, so you can do the configuration you want!


#### Software configuration


Insert the module into the Raspberry Pi, connect the USB interface to the USB port of the Raspberry Pi  and turn it on.
To make the configuration, you will need a monitor, a keyboard, and a mouse. Connect them to the Raspberry Pi 4.
Now, to make the module work, you have to download the minicom.


SIM7600 module is connected to the Raspberry Pi or Jetson Nano through the USB port, and then execute the command to see if the ttyUSB2 can be recognized normally. If possible, open the port through minicom:


* ls /dev/ttyUSB*
* sudo apt-get install minicom
* sudo minicom -D /dev/ttyUSB2


If you follow the steps properly on your screen, you must open a terminal that says at the top, "Welcome to minicom 2.7.1", so send this command to restart the module through minicom:


* AT+CUSBPIDSWITCH=9011,1,1


Give some seconds, and you will see underneath the command appear an "OK" and, after some seconds "+CPIN: READY", "SMS DONE" and "PB DONE".


Now, with the command ifconfig to see if a USB0 network card is recognized (do it in a different terminal):


* inconfig


If you run this command, you have to see USB0, so you have to take the IP address with the command:


* sudo dhclient -v usb0


So now you have to check if you have internet on the Raspberry Pi 4, open a browser, and see if you can navigate a website. If you can navigate the configuration, it is successful if not, follow these steps:


* AT+CREG? (run this on the minicom terminal if you see 0,0 you don't have a connection.)
* AT+CGDCONT? (see the APNs, you have to see the correct APN of your SIM card.)
* AT+CGDCONT=1,"IP","APN" (if you want the APN or add a new one)


Take these steps and try again to navigate a website!


**NOTE**: Your SIM card must have internet data!
