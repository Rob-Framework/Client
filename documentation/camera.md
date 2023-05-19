Connect the Pi camera to the Raspberry Pi 4. On the Raspberry Pi 4 there is a camera modulr port next of the HDMI ports (not the display port). Ensure your Raspberry Pi is turned off 

* Locate the camera module port
* Gently pull up on the edges of the port's plastic clip
* Insert the camera module ribbon cable, make sure the connectors at the bottom of the ribbon cable are facing the contacts in the port
* Push the plastic clip back into place

After that start up your Raspberry Pi. Go to the main menu and open the **Raspberry Pi Configuration** tool, select the **Interfaces** tab and ensure that the camera is enable and lastly reboot the Raspberry Pi.

This is one way to enable your Pi camera.

An other way is to open a terminal and type the command **sudo raspi-config**, this will open another settings, so with the arrows Up and Down select the **Interface Options** -> **Legacy Camera** -> **Yes** -> **Ok**. After that select again the **Interface Option** -> **I2C** -> **Yes** -> **Ok**, lastly check if the serial port is enable. Select again **Interface Option** -> **Serial Port** -> **No** -> **Yes** -> **Ok**, and reboot your Raspberry Pi.

When you finish with the configuration test your Pi camera!