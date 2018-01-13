# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Title: scoredata
# Author: Alex Riviere (github.com/fimion)
# Date: 2017
# Availability: https://github.com/chrisdeely/scoredata/blob/master/python/daktronics.py
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


import serial
class Daktronics(object):
    def __init__(self, sport, com=None):
        if com != None:
            self.Serial = serial.Serial(com, 19200)
        else:
            self.Serial = serial.Serial("COM1", 19200)
        self.header = b''
        self.code = b''
        self.rtd = b''
        self.checksum = b''
        self.text = b''
        self.dakSports = {
            'basketball': {
                'dakSize': [1, 295],
                'Main Clock Time [mm:ss/ss.t]': [1, 5],
                'Main Clock Time [mm:ss.t]': [6, 8],
                'Main Clock/Time Out/TOD [mm:ss/ss.t]': [14, 5],
                'Main Clock/Time Out/TOD [mm:ss.t]': [19, 8],
                'Main Clock =0': [27, 1],
                'Main Clock Stopped': [28, 1],
                'Main Clock/Time Out Horn': [29, 1],
                'Main Clock Horn': [30, 1],
                'Time Out Horn': [31, 1],
                'Time Out Time': [32, 8],
                'Time of Day': [40, 8],
                'Home Team Name': [48, 20],
                'Guest Team Name': [68, 20],
                'Home Team Abbreviation': [88, 10],
                'Guest Team Abbreviation': [98, 10],
                'Home Team Score': [108, 4],
                'Guest Team Score': [112, 4],
                'Home Time Outs Left - Full': [116, 2],
                'Home Time Outs Left - Partial': [118, 2],
                'Home Time Outs Left - Television': [120, 2],
                'Home Time Outs Left - Total': [122, 2],
                'Guest Time Outs Left - Full': [124, 2],
                'Guest Time Outs Left - Partial': [126, 2],
                'Guest Time Outs Left - Television': [128, 2],
                'Guest Time Outs Left - Total': [130, 2],
                'Home Time Out Indicator': [132, 1],
                'Home Time Out Text': [133, 4],
                'Guest Time Out Indicator': [137, 1],
                'Guest Time Out Text': [138, 4],
                'Period': [144, 4],
                'Period Text': [144, 4],
                'Period Description': [148, 12],
                'Internal Relay': [160, 1],
                'Ad Panel / Caption Power': [161, 1],
                'Ad Panel / Caption #1': [162, 1],
                'Ad Panel / Caption #2 ': [163, 1],
                'Ad Panel / Caption #3': [164, 1],
                'Ad Panel / Caption #4': [165, 1],
                'Reserved for Future Use': [166, 35],
                'Shot Clock Time': [201, 8],
                'Shot Clock Horn': [209, 1],
                'Home Possession Indicator': [210, 1],
                'Home Possession Arrow': [211, 1],
                'Home Possession Text': [212, 4],
                'Guest Possession Indicator': [215, 1],
                'Guest Possession Arrow': [216, 4],
                'Guest Possession Text': [218, 4],
                'Home 1-on-1 Bonus Indicator': [222, 1],
                'Home 2-shot Bonus Indicator': [223, 1],
                'Home Bonus Text': [224, 5],
                'Guest 1-on-1 Bonus Indicator': [229, 1],
                'Guest 2-shot Bonus Indicator': [230, 1],
                'Guest Bonus Text': [231, 5],
                'Home Team Fouls': [236, 2],
                'Guest Team Fouls': [238, 2],
                'Home Player-Foul-Points': [240, 8],
                'Guest Player-Foul-Points': [248, 8],
                'Player-Foul': [256, 3],
                'Player-Foul-Points': [259, 5],
                'Home Score - Period 1': [264, 2],
                'Home Score - Period 2': [266, 2],
                'Home Score - Period 3': [268, 2],
                'Home Score - Period 4': [270, 2],
                'Home Score - Current Period': [282, 2],
                'Guest Score - Period 1': [284, 2],
                'Guest Score - Period 2': [286, 2],
                'Guest Score - Period 3': [288, 2],
                'Guest Score - Period 4': [290, 2],
                'Guest Score - Current Period': [302, 2],
                'Guest Score - Period 7': [259, 2],
                'Guest Score - Period 8': [261, 2],
                'Guest Score - Period 9': [263, 2],
                'Guest Score - Current Period': [265, 2],
                'Home Rushing Yards': [267, 4],
                'Home Passing Yards': [271, 4],
                'Home Total Yards': [275, 4],
                'Guest Rushing Yards': [279, 4],
                'Guest Passing Yards': [283, 4],
                'Guest Total Yards': [287, 4],
                'Home First Downs': [291, 2],
                'Guest First Downs': [293, 2]
                }
            }
        self.sport = self.dakSports[sport]
        self.dakString = " " * self.sport['dakSize'][1]

    def update(self):
        c = b''
        self.rtd = b''
        while c != b'\x16':
            c = self.Serial.read()
            #print(c)
        c = b'\x16'
        while c != b'\x17':
            c = self.Serial.read()
            self.rtd += c
            #print(c)

        self.header = self.rtd.partition(b'\x16')[2].partition(b'\x01')[0]
        self.code = self.rtd.partition(b'\x01')[2].partition(b'\x02')[0].partition(b'\x04')[0]
        self.text = self.rtd.partition(b'\x02')[2].partition(b'\x04')[0]
        self.checksum = self.rtd.partition(b'\x04')[2].partition(b'\x17')[0]
        #print("binary:",self.header, self.code, self.text, self.checksum)

        code = self.code.decode()
        code = code[-4:]
        text = self.text.decode()
        #print("code:",code)
        #print("text:",text)
        self.dakString = self.dakString[:int(code)] + text + self.dakString[int(code)+len(text):]

    def __getitem__(self, gikey):
        if gikey in self.sport:
            return self.dakString[self.sport[gikey][0]-1:self.sport[gikey][1]+self.sport[gikey][0]-1]
        return ""
