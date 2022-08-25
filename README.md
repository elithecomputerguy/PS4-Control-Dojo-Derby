# PS4-Control-Dojo-Derby
PS4 Bluetooth control of a dojo derby vehicle

This allows you to directly control a Dojo Derby vehicle with a PS4 controller

Install the pyPS4Controller module to Python - PS4 Python Module - https://pypi.org/project/pyPS4Controller/

Pair the PS4 Controller with the Pi through the standard shell.

For auto start of script add to sudo /etc/rc.local, or to the autostart.py script that is part of the Dojo Derby basic script package.

Then when vehicle boots for headless use, push the PS button on the controller to link the controller with the vehicle within the first 60 seconds after boot.  If you do not do this within 60 seconds the script will time out and the controller will not connect. (Just reboot and try again)
