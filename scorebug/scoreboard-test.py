

# import the scoreboard function
from cctv import scoreboard




dak = {} #define dak to take the sample data

# ************************************************************************************
# Dynampic PNG Variables
# These are the fields that will be poputated by the scoreboard console
# ************************************************************************************

dak['Home Team Score']= '00'
dak['Home Time Outs Left - Total'] = '3'
dak['Home Team Fouls'] = '0'
dak['Home Bonus Text'] = 'BONUS'
dak['Home Possession Text'] = 'POSS'
dak['Home Time Out Text'] = 'TIME'

dak['Guest Team Score'] = '1'
dak['Guest Time Outs Left - Total'] = '3'
dak['Guest Team Fouls'] = '10'
dak['Guest Bonus Text'] = 'BONUS'
dak['Guest Possession Text'] = 'POSS'
dak['Guest Time Out Text'] = 'TIME'

dak['Period'] = '1st'
dak['Main Clock Time [mm:ss/ss.t]'] = '10:00'
dak['Shot Clock Time'] = '9'
dak['Time Out Time'] = ''

dak['Home Player-Foul-Points']='00-00-00'
dak['Guest Player-Foul-Points']='00-00-00'
dak['Player-Foul']='000'
dak['Player-Foul-Points']='00000'

ShowPlayerFoul = True

# ************************************************************************************

scoreboard(dak,ShowPlayerFoul,True)




