# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:49:45 2019

@author: bhatt
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("data.csv") #Do not spoil this dataset
df=dataset

df['GoalKeeper']=df.GKDiving+df.GKHandling+df.GKKicking+df.GKPositioning+df.GKReflexes+df.LongPassing+df.LongShots+df.Jumping
GoalKeeper = df[df['Position'] == 'GK'].sort_values('GoalKeeper', ascending=False)[:18207]


df['CentralDefender']=4*(df.Strength+df.Reactions+df.Crossing+df.Aggression)+5*(df.Marking+df.HeadingAccuracy+df.Interceptions+df.SlidingTackle+df.StandingTackle) + 3*(df.Acceleration+df.SprintSpeed+df.ShotPower+df.LongShots)+2*(df.BallControl+df.Stamina+df.Jumping+df.FKAccuracy)+df.Vision+df.ShortPassing+df.LongPassing
CentralDefender = df.sort_values('CentralDefender', ascending=False)[:18207]
LeftCentralDefender= df[(df['Position'] == 'LCB') | (df['Position'] == 'CB')].sort_values('CentralDefender', ascending=False)[:18207]
RightCentralDefender= df[(df['Position'] == 'RCB') | (df['Position'] == 'CB')].sort_values('CentralDefender', ascending=False)[:18207]

df['WingBack'] = 4*(df.Strength+df.Reactions+df.Crossing+df.Stamina+df.LongPassing+df.Vision)+5*(df.Interceptions+df.SlidingTackle+df.StandingTackle+df.Acceleration+df.SprintSpeed) + 3*(df.ShotPower+df.LongShots)+2*(df.BallControl+df.Jumping+df.FKAccuracy)+df.Aggression+df.ShortPassing+df.Marking
LeftWingBack = df[(df['Position'] == 'LWB') | (df['Position'] == 'LB')].sort_values('WingBack', ascending=False)[:18207]
RightWingBack = df[(df['Position'] == 'RWB') | (df['Position'] == 'RB')].sort_values('WingBack', ascending=False)[:18207]

df['CentralMid'] = 5*(df.BallControl+df.Dribbling+df.Reactions+df.Vision+df.ShortPassing)+4*(df.Crossing+df.Curve+df.FKAccuracy)+3*(df.LongPassing)+2*(df.LongShots)+df.Marking
CentralMid = df[(df['Position'] == 'CAM') | (df['Position'] == 'LAM') | (df['Position'] == 'RAM')].sort_values('CentralMid', ascending=False)[:18207]

df['RightMid'] = 5*(df.Agility+df.Stamina+df.ShortPassing+df.Reactions) + 4*(df.Balance+df.Strength+df.Acceleration+df.Aggression) + 3*(df.Jumping+df.Marking+df.StandingTackle+df.SlidingTackle+df.Interceptions)+df.SprintSpeed
RightMid = df[(df['Position'] == 'RCM') | (df['Position'] == 'RM')].sort_values('RightMid', ascending=False)[:18207]

df['LeftMid'] = 5*(df.BallControl+df.ShortPassing+df.LongPassing)+ 4*(df.Vision+df.Composure)+df.Dribbling+df.Marking+df.Reactions
LeftMid = df[(df['Position'] == 'LCM') | (df['Position'] == 'LM')].sort_values('LeftMid', ascending=False)[:18207]

df['Striker']= 5*(df.Balance+df.Finishing+df.HeadingAccuracy) + 4*(df.Jumping+df.Dribbling) + 3*(df.BallControl+df.Aggression+df.Agility) + df.Vision+df.Curve+df.LongShots
Striker= df[(df['Position'] == 'ST') | (df['Position'] == 'LS') | (df['Position'] == 'RS') | (df['Position'] == 'CF')].sort_values('Striker', ascending=False)[:18207]

df['WingForward']= 5*(df.Finishing+df.HeadingAccuracy+df.Acceleration) + 4*(df.LongShots+df.Crossing+df.Dribbling+df.BallControl+df.SprintSpeed) + 3*(df.FKAccuracy+df.Aggression+df.Agility+df.Vision+df.ShortPassing+df.LongPassing)+df.Curve
LeftForward= df[(df['Position'] == 'LW') | (df['Position'] == 'LM') | (df['Position'] == 'LS') | (df['Position'] == 'LF')].sort_values('WingForward', ascending=False)[:18207]
RightForward= df[(df['Position'] == 'RW') | (df['Position'] == 'RM') | (df['Position'] == 'RS') | (df['Position'] == 'RF')].sort_values('WingForward', ascending=False)[:18207]

#Number of players:
tName1 = 'Real Madrid'
tName2 = 'FC Barcelona'
team1 = pd.DataFrame(df[(df['Club'] == tName1)])
team2 = pd.DataFrame(df[(df['Club'] == tName2)])
teamDict = {}
gk = pd.DataFrame(GoalKeeper[(GoalKeeper['Club'] == tName1) | (GoalKeeper['Club'] == tName2)])
teamDict['GK'] = gk.to_dict('list')['Name']
lcd = pd.DataFrame(LeftCentralDefender[(LeftCentralDefender['Club'] == tName1) | (LeftCentralDefender['Club'] == tName2)])
teamDict['LCD'] = lcd.to_dict('list')['Name']
rcd = pd.DataFrame(RightCentralDefender[(RightCentralDefender['Club'] == tName1) | (RightCentralDefender['Club'] == tName2)])
teamDict['RCD'] = rcd.to_dict('list')['Name']
lwb = pd.DataFrame(LeftWingBack[(LeftWingBack['Club'] == tName1) | (LeftWingBack['Club'] == tName2)])
teamDict['LWB'] = lwb.to_dict('list')['Name']
rwb = pd.DataFrame(RightWingBack[(RightWingBack['Club'] == tName1) | (RightWingBack['Club'] == tName2)])
teamDict['RWB'] = rwb.to_dict('list')['Name']
cm = pd.DataFrame(CentralMid[(CentralMid['Club'] == tName1) | (CentralMid['Club'] == tName2)])
teamDict['CM'] = cm.to_dict('list')['Name']
rm = pd.DataFrame(RightMid[(RightMid['Club'] == tName1) | (RightMid['Club'] == tName2)])
teamDict['RM'] = rm.to_dict('list')['Name']
lm = pd.DataFrame(LeftMid[(LeftMid['Club'] == tName1) | (LeftMid['Club'] == tName2)])
teamDict['LM'] = lm.to_dict('list')['Name']
st = pd.DataFrame(Striker[(Striker['Club'] == tName1) | (Striker['Club'] == tName2)])
teamDict['ST'] = st.to_dict('list')['Name']
lf = pd.DataFrame(LeftForward[(LeftForward['Club'] == tName1) | (LeftForward['Club'] == tName2)])
teamDict['LF'] = lf.to_dict('list')['Name']
rf = pd.DataFrame(RightForward[(RightForward['Club'] == tName1) | (RightForward['Club'] == tName2)])
teamDict['RF'] = rf.to_dict('list')['Name']

allstar = pd.DataFrame.from_dict(teamDict, orient = 'index')
allstar = allstar.transpose()
