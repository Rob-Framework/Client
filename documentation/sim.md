## Connect the Waveshare SIM7600E-H 4G HAT

The Waveshare SIM7600E-H 4G HAT is a module that enables internet connectivity, making calls, and sending messages through the Raspberry Pi 4. The connection process is relatively simple.

1.Start by connecting the SIM card to the module. The SIM card slot is located on the backside of the module.
2.Connect the USB cable to the module, which will establish a connection with the Raspberry Pi 4.
3.Attach the GPS module to the front side of the SIM7600E-H module.
4.Additionally, you can connect an LTE antenna to the front side of the module for better signal reception.
5.Optionally, you can connect headphones or a TF card to the module.

There are a few important considerations regarding jumpers on the module:

* In the new version, the PWR and 3V3 pins are short-circuited by default, allowing the HAT to turn on automatically after connecting the power supply.
* If you wish to use the PWRKEY button to control the HAT's power, remove the jumper cap between PWR and 3V3.
* To enable Raspberry Pi control for turning the HAT on/off, set the jumper cap between PWR and D6.
* If you need to control the flight mode through the Raspberry Pi pins, set the jumper cap between Flight and D4.
Software Configuration
To configure the module, follow these steps:

1. Insert the module into the Raspberry Pi and connect the USB interface to one of the Raspberry Pi's USB ports.
2. Connect a monitor, keyboard, and mouse to the Raspberry Pi 4 for configuration purposes.
3. Download and install minicom on the Raspberry Pi using the following commands:
    ls /dev/ttyUSB*
    sudo apt-get install minicom
    sudo minicom -D /dev/ttyUSB2
4. If the previous steps were executed correctly, the minicom terminal should open with the message "Welcome to minicom 2.7.1". To restart the module through minicom, enter the command:
    AT+CUSBPIDSWITCH=9011,1,1
Wait a few seconds for the response, which should include "OK," "+CPIN: READY," "SMS DONE," and "PB DONE."

5. Open another terminal and use the command ifconfig to check if a USB0 network card is recognized. You should see USB0 listed. Retrieve the IP address using the command:
    sudo dhclient -v usb0
6. Verify if you have internet connectivity on the Raspberry Pi 4 by opening a browser and navigating to a website. If you can access the website, the configuration was successful. If not, follow these additional steps:

    AT+CREG? # Check if the response shows 0,0, which indicates no connection
    AT+CGDCONT? # Verify the APN settings; ensure the correct APN for your SIM card is displayed
    AT+CGDCONT=1,"IP","APN" # Use this command to set the APN or add a new one
7. After following these steps, try accessing a website again to confirm internet connectivity.
Note: Ensure that your SIM card has an active internet data plan for successful connectivity.

#### Debugging

If you decide to connect a sensor on the GPIOs of the SIM7600, you may have some issues, and your sensor may not work properly. So the only thing you have to do is disconnect the SIM7600 from the GPIOs of the Raspberry Pi and keep only the connection with the USB cable. After that, you have to remove the jumper from PWM-D6 pins to PWM-3V3. That way, you can connect any sensor straight to the Raspberry Pi and avoid issues with your sensor and you can have access to the mobile data of your SIM module.