from daktronics import Daktronics
import time, config
# import the scoreboard function
from advanced import scoreboard

# Define COM Port
COMPort = "COM1"

dak = Daktronics("basketball", COMPort)


while True:
    try: 
        dak.update()
        scoreboard(dak)
    except KeyboardInterrupt:
        print("--------------------")
        print("-- Program Halted --")
        print("--------------------")
        break
