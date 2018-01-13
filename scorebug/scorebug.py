from daktronics import Daktronics
import time, config
# import the scoreboard function
from default import scoreboard

# Define COM Port
COMPort = "COM3"

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
