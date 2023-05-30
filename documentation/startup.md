To ensure that your robot framework runs automatically every time the Raspberry Pi reboots, you can use the pm2 software. Follow these steps to install and configure pm2 on your Raspberry Pi:

**Note: Make sure you have Node.js installed on your Raspberry Pi before proceeding.**

1. Install pm2 on your Raspberry Pi by running the following command:
    sudo npm install pm2 -g
2. Optionally, you can install CLI autocompletion for pm2 by running:
    pm2 completion install
3. To use pm2, run the following command:
    pm2 startup
This command will output a response similar to: sudo env PATH=$PATH:/usr/local/bin pm2 startup -u safeuser. Copy and paste the provided command into the same terminal.

1. Navigate to the path of your repository by running:
    cd <repository_path>
2. Start your script with pm2 using the following command:
    pm2 start src/index.js
3. To verify that your script is running in the background, you can check the list of pm2 processes by running:
    pm2 list
This command will display a panel with information about your script.

1. To view real-time logs of your script, use the following command:
    pm2 logs
2. After making changes, save the pm2 configuration by running:
    pm2 save
3. Now, if you reboot your Raspberry Pi or turn it off, your script will automatically run in the background upon reboot.
To stop your script, use the following command:
    pm2 stop <script_id>
Replace <script_id> with the actual ID of your script, which you can find from the pm2 list command.

To delete your script from the pm2 list, use the following command:
    pm2 delete <script_id>
Again, replace <script_id> with the actual ID of your script.

You can always check the status of your scripts by running pm2 list.