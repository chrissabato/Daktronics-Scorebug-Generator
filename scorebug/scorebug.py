from daktronics import Daktronics

# import the scoreboard function
from default import scoreboard

# Define folder loaction
FolderLoc = "D:\\GitHub\\Daktronics-Scorebug-Generator\\scorebug\\"

# Define COM Port
#COMPort = "COM7"

dak = Daktronics("basketball")
#dak = Daktronics("basketball", COMPort)

while True:
    dak.update()
    scoreboard(dak,FolderLoc,True)
