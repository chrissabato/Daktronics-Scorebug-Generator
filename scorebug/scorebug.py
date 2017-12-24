from daktronics import Daktronics

# import the scoreboard function
from cctv import scoreboard

# Define folder loaction
FolderLoc = "D:\\GitHub\\Daktronics-Scorebug-Generator\\scorebug\\"

# Define COM Port
ser = {"COM1", 19200}

dak = Daktronics("basketball")
while True:
    dak.update()
    scoreboard(dak,FolderLoc,True)
