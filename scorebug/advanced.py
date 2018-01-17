# ////////////////////////////////////////////////////////////////////////////////////
# ************************************************************************************
# Scoreboard Creation Function
# ************************************************************************************
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import json,re,datetime,config,time
from PIL import Image, ImageDraw, ImageFont

def scoreboard(dak):

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

  HomePlayerFoulPoints = dak['Home Player-Foul-Points'].strip()
  AwayPlayerFoulPoints = dak['Guest Player-Foul-Points'].strip()




  #Define Colors
  font_Color = "#ffffff"
  font_Color2 = "#000000"
  TimeOutAvailableColor="#272727"
  TimeOutUsedColor="#ffffff"
  TimeOutClockColor="#483281"
  TimeOutClockFontColor="#ffffff"
  TimeOutBackgroundColor="#9999cc"
  BonusColor="#ccff00"
  PossColor=TimeOutAvailableColor
  PossTextColor="#ffffff"
  ShotClockColor="#ffffff"
  ShotClockAlertColor="#ccff00"

  # Load setup data
  setupdata = json.load(open("scorebug-setup.json"))



  HomeTeamName = setupdata["HomeTeamName"]
  HomeTeamRank = setupdata["HomeTeamRank"]
  HomeTeamColor = setupdata["HomeTeamColor"]
  HomeTeamColor2 = setupdata["HomeTeamColor2"]
  AwayTeamName = setupdata["AwayTeamName"]
  AwayTeamRank = setupdata["AwayTeamRank"]
  AwayTeamColor = setupdata["AwayTeamColor"]
  AwayTeamColor2 = setupdata["AwayTeamColor2"]
  Venue = setupdata["Venue"]
  ClockBackgroundColor = setupdata["ClockBackgroundColor"]
  NetworkLogo = setupdata["NetworkLogo"]
  UseRoster = setupdata["UseRoster"]

  if UseRoster:
    # Load Roster Data
    roster = json.load(open("rosters.json"))

  # Draw Background
  img1 = Image.new('RGBA',(1400, 120))
  drawbg = ImageDraw.Draw(img1)
  drawbg.rectangle(((100, 40), (499, 96)), fill=AwayTeamColor)             # Away team background
  drawbg.rectangle(((600, 40), (999, 96)), fill=HomeTeamColor)             # Home team background
  drawbg.rectangle(((1000, 40), (1299, 96)), fill=ClockBackgroundColor)              # Clock background
  #drawbg.rectangle(((0, 97), (1299, 119)), fill=TimeOutBackgroundColor)    # Timeout background

  # Import Transparent Background
  img2 = Image.open('Images\\advanced.png')

  # Import Logos
  # Away Team Logo
  imgName = re.sub('[^0-9a-zA-Z]+', '', AwayTeamName)
  awayImg = Image.open('Logos\\' + imgName + ".png")
  img2.paste(awayImg,(0,40))
  # Away Team Logo
  imgName = re.sub('[^0-9a-zA-Z]+', '', HomeTeamName)
  homeImg = Image.open("Logos\\" + imgName + ".png")
  img2.paste(homeImg,(500,40))
  # Network Logo
  logoImg = Image.open("Logos\\"+NetworkLogo)
  img2.paste(logoImg,(1310,40))

  # Composite the two background images
  image = Image.new('RGBA',(1380, 120))
  image = Image.alpha_composite(img1, img2)
  draw = ImageDraw.Draw(image)

  # Define Fonts
  font_TeamName = ImageFont.truetype('Fonts\\'+'AvenirNextCondensed-DemiBold.ttf',36)
  font_Rank = ImageFont.truetype('Fonts\\'+'AvenirNextCondensed-Medium.ttf',24)
  font_Score = ImageFont.truetype('Fonts\\'+'AvenirNextCondensed-DemiBold.ttf',46)
  font_clock = ImageFont.truetype('Fonts\\'+'AvenirNextCondensed-DemiBold.ttf',40)
  font_gameClock = ImageFont.truetype('Fonts\\'+'AvenirNextCondensed-DemiBold.ttf',46)
  font_venue = ImageFont.truetype('Fonts\\'+'AvenirNext-Medium.ttf',20)
  font_TO = ImageFont.truetype('Fonts\\'+'AvenirNext-Heavy.ttf',60)
  font_fouls = ImageFont.truetype('Fonts\\'+'AvenirNextCondensed-DemiBold.ttf',18)
  font_poss = ImageFont.truetype('Fonts\\'+'AvenirNextCondensed-DemiBold.ttf',18)
  font_toclock = ImageFont.truetype('Fonts\\'+'AvenirNextCondensed-DemiBold.ttf',18)
  font_PlayerFoul = ImageFont.truetype('Fonts\\'+'AvenirNextCondensed-Medium.ttf',22)

  # ----------------------------
  # Away Team
  # ----------------------------

  # Name
  w, h = 0, 0
  if AwayTeamRank != "":
    draw.text(xy=(105,57),text=AwayTeamRank,fill=AwayTeamColor2,font=font_Rank)  
    w, h = draw.textsize(AwayTeamRank,font_Rank)
  draw.text(xy=(110+(w-3),45),text=AwayTeamName.upper(),fill=AwayTeamColor2,font=font_TeamName)

  # Score 
  AwayTeamScore = AwayTeamScore.strip()
  w, h = draw.textsize(AwayTeamScore,font_Score)
  xpos = 463-w/2
  draw.text(xy=(xpos,40),text=AwayTeamScore,fill=font_Color,font=font_Score)

  # Timeouts

  draw.text(xy=(110,67),text="————",fill=TimeOutUsedColor,font=font_TO)
  DisplayTO = ""
  try:
      AwayTOL = int(AwayTOL)
  except ValueError as verr:
      AwayTOL = 0
  for x in range(AwayTOL):
      DisplayTO = DisplayTO + "—"
  draw.text(xy=(110,67),text=DisplayTO,fill=TimeOutAvailableColor,font=font_TO)
  if AwayTimeOut == "TIME":
      draw.rectangle(((265, 97), (374, 120)), fill=TimeOutClockColor)
      draw.text(xy=(275,97),text="TIME OUT :"+TimeOutClock,fill=TimeOutClockFontColor,font=font_toclock)
      
  # Fouls
  DisplayFouls = AwayFouls.strip()+ " FOULS"
  if AwayBonus == "BONUS":
      draw.rectangle(((430, 40), (499, 43)), fill=BonusColor)
      draw.rectangle(((430, 97), (499, 120)), fill=BonusColor)

  w, h = draw.textsize(DisplayFouls,font_fouls)
  xpos = 464-w/2    
  draw.text(xy=(xpos,97),text=DisplayFouls,fill=font_Color2,font=font_fouls)

  # Possession
  if AwayPossession == "POSS":
      draw.rectangle(((375, 97), (429, 120)), fill=PossColor)
      draw.text(xy=(385,97),text="POSS",fill=PossTextColor,font=font_poss)

      
  # ----------------------------
  # Home Team
  # ----------------------------

  # Name
  w, h = 0, 0
  if HomeTeamRank != "":
    draw.text(xy=(605,57),text=HomeTeamRank,fill=HomeTeamColor2,font=font_Rank)  
    w, h = draw.textsize(HomeTeamRank,font_Rank)
  draw.text(xy=(610+(w-3),45),text=HomeTeamName.upper(),fill=HomeTeamColor2,font=font_TeamName)

  # Score
  HomeTeamScore = HomeTeamScore.strip()
  w, h = draw.textsize(HomeTeamScore,font_Score)
  xpos = 965-w/2
  draw.text(xy=(xpos,40),text=HomeTeamScore,fill=font_Color,font=font_Score)

  # Timeouts
  draw.text(xy=(610,67),text="————",fill=TimeOutUsedColor,font=font_TO)
  DisplayTO = ""
  try:
      HomeTOL = int(HomeTOL)
  except ValueError as verr:
      HomeTOL = 0
  for x in range(HomeTOL):
      DisplayTO = DisplayTO + "—"
  draw.text(xy=(610,67),text=DisplayTO,fill=TimeOutAvailableColor,font=font_TO)
  if HomeTimeOut == "TIME":
      draw.rectangle(((765, 97), (874, 120)), fill=TimeOutClockColor)
      draw.text(xy=(775,97),text="TIME OUT :"+TimeOutClock,fill=TimeOutClockFontColor,font=font_toclock)

  # Fouls
  DisplayFouls = HomeFouls.strip()+ " FOULS"
  if HomeBonus == "BONUS":
      draw.rectangle(((930, 40), (999, 43)), fill=BonusColor)
      draw.rectangle(((930, 97), (999, 120)), fill=BonusColor)
  w, h = draw.textsize(DisplayFouls,font_fouls)
  xpos = 965-w/2    
  draw.text(xy=(xpos,97),text=DisplayFouls,fill=font_Color2,font=font_fouls)

  # Possession
  if HomePossession == "POSS":
      draw.rectangle(((875, 97), (929, 120)), fill=PossColor)
      draw.text(xy=(885,97),text="POSS",fill=PossTextColor,font=font_poss)

  #Venue 
  w, h = draw.textsize(Venue.upper(),font_venue)
  xpos = 1150-w/2
  draw.text(xy=(xpos,95),text=Venue.upper(),fill=font_Color,font=font_venue)


  #Period
  w, h = draw.textsize(Period,font_clock)
  xpos = 1050-w/2
  draw.text(xy=(xpos,42),text=Period,fill=font_Color,font=font_clock)

  #Clock
  w, h = draw.textsize(Clock,font_clock)
  xpos = 1165-w/2
  draw.text(xy=(xpos,42),text=Clock,fill=font_Color,font=font_gameClock)

  #ShotClock
  try:
      if int(ShotClock) < 10:
          ShotClockColor=ShotClockAlertColor
  except:
     ShotClockColor=ShotClockColor
     
  w, h = draw.textsize(ShotClock,font_clock)
  xpos = 1270-w/2
  draw.text(xy=(xpos,42),text=ShotClock,fill=ShotClockColor,font=font_clock)      





  # Home Player Foul Display
  if config.HomeLastPlayerFoul != HomePlayerFoulPoints:
    config.HomeLastPlayerFoul = HomePlayerFoulPoints
    config.HomePlayerFoulClockStart = time.clock()
    print("New Home Foul :" + HomePlayerFoulPoints)
    
  if time.clock() < config.HomePlayerFoulClockStart + 10 and HomePlayerFoulPoints.strip() != '' :
      #print("Show Home Foul")
      HomeFouls = HomePlayerFoulPoints.split("-")
      TmpNum = HomeFouls[0].strip()
      TmpFoulCount = HomeFouls[1].strip()
      try:
        dispString = TmpNum + "  " +roster['home'][TmpNum]
      except:
        dispString = TmpNum + "  " +HomeTeamName.upper()
  
      draw.rectangle(((600, 5), (659, 34)), fill="#000000")
      draw.rectangle(((660, 5), (999, 34)), fill="#444444")
      draw.text(xy=(609,6),text="Foul".upper(),fill=BonusColor,font=font_PlayerFoul)
      draw.text(xy=(669,6),text=dispString.upper(),fill="#FFFFFF",font=font_PlayerFoul)

      w, h = draw.textsize(dispString.upper(),font_PlayerFoul)
      for x in range(int(TmpFoulCount)):
        draw.rectangle( ( (680 + w + (15*x), 15), (689+w + (15*x), 24) ), fill=BonusColor)
        


  # Away Player Foul Display
  if config.AwayLastPlayerFoul != AwayPlayerFoulPoints:
    config.AwayLastPlayerFoul = AwayPlayerFoulPoints
    config.AwayPlayerFoulClockStart = time.clock()
    print("New Away Foul :" + AwayPlayerFoulPoints)
    
  if time.clock() < config.AwayPlayerFoulClockStart + 10 and AwayPlayerFoulPoints.strip() != '':
      #print("Show Away Foul")
      AwayFouls = AwayPlayerFoulPoints.split("-")
      TmpNum = AwayFouls[0].strip()
      TmpFoulCount = AwayFouls[1].strip()
      try:
        dispString = TmpNum + "  " +roster['away'][TmpNum]
      except:
        dispString = TmpNum + "  " +AwayTeamName.upper()
  
      draw.rectangle(((100, 5), (159, 34)), fill="#000000")
      draw.rectangle(((160, 5), (499, 34)), fill="#444444")
      draw.text(xy=(109,6),text="Foul".upper(),fill=BonusColor,font=font_PlayerFoul)
      draw.text(xy=(169,6),text=dispString.upper(),fill="#FFFFFF",font=font_PlayerFoul)

      w, h = draw.textsize(dispString.upper(),font_PlayerFoul)
      for x in range(int(TmpFoulCount)):
        draw.rectangle( ( (180 + w + (15*x), 15), (189+w + (15*x), 24) ), fill=BonusColor)
        







    
        
  try:
      image.save("scorebug.png","PNG")
  except:
      print("Error Saving")


  print(Clock)

  return ''
