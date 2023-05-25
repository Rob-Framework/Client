To make your robot independent, you have to find a way to run the framework every time it reboots. So for this issue, you will need to use **pm2** software. First of all, you have to install it on your Raspberry Pi, following this command:


**Note: You have to install NodeJS on your Raspberry Pi!**


* sudo npm install pm2 -g


By default, CLI autocompletion is not installed with PM2, but i recommend it:


* pm2 completion install


Now to use the pm2 is easy first of all, run this command:


* pm2 startup


You will see a response like : **sudo env PATH=$PATH:/usr/local/bin pm2 startup -u safeuser** so copy/paste this command on the same terminal, and after that, run this command:


* cd <repsitory_path>
* pm2 start src/index.js


To be sure, you can check if your script runs in the background with this command:


* pm2 list


You will see a panel with information about your script. To display logs in real time, run this command:


* pm2 logs


When you finish, you have to save, run this command:


* pm2 save


So now if you reboot your Raspberry Pi or turn it off for some reason, your script will run in the background every time you reboot your Raspberry Pi.


If you want to stop your script, type this command:


* pm2 stop (and the id of your script (you can see it from the command pm2 list))


If you want to delete your script from the list, type this command:


* pm2 delete (and the id of your script (you can see it from the command pm2 list))


To check if you deleted or stopped your script, check with the **pm2 list**

