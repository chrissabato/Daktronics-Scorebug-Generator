# ////////////////////////////////////////////////////////////////////////////////////
# ************************************************************************************
# Scoreboard Creation Function
# ************************************************************************************
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import json,re 
from PIL import Image, ImageDraw, ImageFont

def scoreboard(dak,FolderLoc, FullConsoleDetails = False):

    # ****************************
    # Dynampic PNG Variables
    # ****************************

    HomeTeamScore = dak['Home Team Score']
    HomeTOL = dak['Home Time Outs Left - Total']
    HomeFouls = dak['Home Team Fouls']
    HomeBonus = dak['Home Bonus Text']
    HomePossession=dak['Home Possession Text']
    HomeTimeOut=dak['Home Time Out Text']

    AwayTeamScore = dak['Guest Team Score']
    AwayTOL = dak['Guest Time Outs Left - Total']
    AwayFouls = dak['Guest Team Fouls']
    AwayBonus = dak['Guest Bonus Text']
    AwayPossession=dak['Guest Possession Text']
    AwayTimeOut=dak['Guest Time Out Text']

    Period = dak['Period']
    Clock = dak['Main Clock Time [mm:ss/ss.t]']
    ShotClock = dak['Shot Clock Time'].strip()
    TimeOutClock = dak['Time Out Time']
    TimeOutClock = TimeOutClock.strip().rjust(2,'0')

    #Define Colors
    ScoreColor = "#ffffff"
    PeriodColor = "#ffffff"
    font_Color2 = "#000000"
    TimeOutColor="#cccccc"
    TimeOutUsedColor="#272727"
    TimeOutClockColor="#00ff33"
    TimeOutClockFontColor=TimeOutColor
    BonusColor="#ccff00"
    PossColor=TimeOutColor
    PossTextColor=BonusColor
    ShotClockColor="#ffffff"
    ClockColor="#ccff00"

    # Load setup data
    setupdata = json.load(open(FolderLoc+"scorebug-setup.json"))

    HomeTeamName=setupdata["HomeTeamName"]
    HomeTeamRank=setupdata["HomeTeamRank"]
    HomeTeamColor=setupdata["HomeTeamColor"]
    HomeTeamColor2=setupdata["HomeTeamColor2"]
    AwayTeamName=setupdata["AwayTeamName"]
    AwayTeamRank=setupdata["AwayTeamRank"]
    AwayTeamColor=setupdata["AwayTeamColor"]
    AwayTeamColor2=setupdata["AwayTeamColor2"]
    Venue=setupdata["Venue"]
    ClockBackgroundColor=setupdata["ClockBackgroundColor"]



    # Draw Background
    img1 = Image.new('RGBA',(1140, 80))
    drawbg = ImageDraw.Draw(img1)
    drawbg.rectangle(((0, 0), (499, 79)), fill=AwayTeamColor)
    drawbg.rectangle(((500, 0), (639, 79)), fill=ClockBackgroundColor)
    drawbg.rectangle(((640, 0), (1139, 79)), fill=HomeTeamColor)

    # Import Transparent Background
    img2 = Image.open(FolderLoc+'Images\\default.png')

    # Composite the two background images
    image = Image.new('RGBA',(1100, 80))
    image = Image.alpha_composite(img1, img2)

    draw = ImageDraw.Draw(image)

    # Define Fonts
    font_TeamName = ImageFont.truetype(FolderLoc+'Fonts\\Arial Narrow Bold.ttf',38)
    font_Rank = ImageFont.truetype(FolderLoc+'Fonts\\Arial Narrow Bold.ttf',36)
    font_Score = ImageFont.truetype(FolderLoc+'Fonts\\Arial Narrow Bold.ttf',70)
    font_Clock = ImageFont.truetype(FolderLoc+'Fonts\\Arial Narrow Bold.ttf',36)
    font_TimeOuts = ImageFont.truetype(FolderLoc+'Fonts\\Arial Black.ttf',40)
    font_Period = ImageFont.truetype(FolderLoc+'Fonts\\Arial Narrow Bold.ttf',24)

    # ----------------------------
    # Away Team
    # ----------------------------

    # Name
    w, h = draw.textsize(AwayTeamName.upper(),font_TeamName)
    draw.text(xy=(360-w,18),text=AwayTeamName.upper(),fill=AwayTeamColor2,font=font_TeamName)

    # Score
    AwayTeamScore = AwayTeamScore.strip()
    w, h = draw.textsize(AwayTeamScore,font_Score)
    xpos = 435-w/2
    draw.text(xy=(xpos,0),text=AwayTeamScore,fill=ScoreColor,font=font_Score)

    # Timeouts
    y=36
    try:
        AwayTOL = int(AwayTOL)
    except ValueError as verr:
        AwayTOL = 0
    for x in range(0, 4):
        if x<AwayTOL:
            tmp = TimeOutColor
        else:
            tmp = TimeOutUsedColor
        draw.text(xy=(505,y),text=u"\u2022",fill=tmp,font=font_TimeOuts)
        y = y-18



    # ----------------------------
    # Home Team
    # ----------------------------

    # Name
    w, h = draw.textsize(HomeTeamName,font_TeamName)
    draw.text(xy=(780,18),text=HomeTeamName.upper(),fill=HomeTeamColor2,font=font_TeamName)

    # Score
    HomeTeamScore = HomeTeamScore.strip()
    w, h = draw.textsize(HomeTeamScore,font_Score)
    xpos = 704-w/2
    draw.text(xy=(xpos,0),text=HomeTeamScore,fill=ScoreColor,font=font_Score)

    # Timeouts
    y=36
    try:
        HomeTOL = int(HomeTOL)
    except ValueError as verr:
        HomeTOL = 0
    for x in range(0, 4):
        if x<HomeTOL:
            tmp = TimeOutColor
        else:
            tmp = TimeOutUsedColor
        draw.text(xy=(615,y),text=u"\u2022",fill=tmp,font=font_TimeOuts)
        y = y-18

    #Period
    w, h = draw.textsize(Period,font_Period)
    xpos = 550-w/2
    draw.text(xy=(xpos,50),text=Period,fill=PeriodColor,font=font_Period)

    #Clock
    w, h = draw.textsize(Clock,font_Clock)
    xpos = 570-w/2
    draw.text(xy=(xpos,5),text=Clock,fill=ClockColor,font=font_Clock)

    #ShotClock
    w, h = draw.textsize(ShotClock,font_Period)
    xpos = 595-w/2
    draw.text(xy=(xpos,50),text=ShotClock,fill=ShotClockColor,font=font_Period)      

    try:
        image.save(FolderLoc+"scorebug.png","PNG")
    except:
        print("Error Saving")



    if FullConsoleDetails:
        print("\n\n\n")
        print("_______________________________________________________________")
        print("Clock:          " + Clock)
        print("Shot Clock:     " + ShotClock)
        print("Time Out Clock: " + TimeOutClock)
        print("Period:         " + Period)
        print("Teams           | " + AwayTeamName.ljust(20) + "| "+ HomeTeamName)
        print("Score           | " + AwayTeamScore.ljust(20) + "| "+ HomeTeamScore)
        print("Time Outs L     | " + str(AwayTOL).ljust(20) + "| "+ str(HomeTOL))
        print("Time Out        | " + AwayTimeOut.ljust(20) + "| "+ HomeTimeOut)
        print("Fouls           | " + AwayFouls.strip().ljust(20) + "| "+ HomeFouls.strip())
        print("Bounus          | " + AwayBonus.ljust(20) + "| "+ HomeBonus)
        print("Possesion       | " + AwayPossession.ljust(20) + "| "+ HomePossession)
    else:
        print(Clock)

    return ''




