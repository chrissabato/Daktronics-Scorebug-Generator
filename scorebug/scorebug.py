from daktronics import Daktronics

# import the scoreboard function
from default import scoreboard

# Define COM Port
COMPort = "COM7"

#dak = Daktronics("basketball")
dak = Daktronics("basketball", COMPort)

while True:
    try: 
        dak.update()
        scoreboard(dak,FolderLoc,True)
    except:
        break
