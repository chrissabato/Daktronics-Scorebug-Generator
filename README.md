# Daktronics Scorebug Generator

These python scripts will generate a png scorebug from te RTD data taken from an Daktronics All Sport 5000 controller.

## Files
### scoreboard-test.py
This is used to test you scoreboard creation. It does not require a serial connection. The test data can be defined in the script

### scorebug-setup.json
This is the setup file for the scoreboard. This can be used to modify things like colors and team names.

### scorebug.py
This is the full file, this will parse the serial data and create the scorebug png file.

## Setup

### Connections
Use a DB25/M to DB9/F Null modem cable to connect to a serial port on you computer. Set you COM port to the following settings.
* **Bits persecond:** 19200
* **Data bits:** 8
* **Parity:* None
* **Stop bits:** 1
* **Flow controll:** None

### Software
Install the latest version of Python. Also install the folowing modules.
* pyserial
* Pillow

### Configure scripts
The script location must be defined. Weather you using scoreboard-test.py or scorebug.py the location of the script files need to be set in each file. The variable is called *FolderLoc* and is located on line 7 of each file.

By default the scorebug.py file uses COM1, to change that you need to uncomment lines 10 and 13 and comment line 12
