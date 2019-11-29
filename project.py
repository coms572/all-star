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
teamDict[0] = gk.to_dict('list')['Name']
#0 GoalKeeper
lcd = pd.DataFrame(LeftCentralDefender[(LeftCentralDefender['Club'] == tName1) | (LeftCentralDefender['Club'] == tName2)])
teamDict[1] = lcd.to_dict('list')['Name']
#1 LCD
rcd = pd.DataFrame(RightCentralDefender[(RightCentralDefender['Club'] == tName1) | (RightCentralDefender['Club'] == tName2)])
teamDict[2] = rcd.to_dict('list')['Name']
#2 RCD
lwb = pd.DataFrame(LeftWingBack[(LeftWingBack['Club'] == tName1) | (LeftWingBack['Club'] == tName2)])
teamDict[3] = lwb.to_dict('list')['Name']
#3 LWB
rwb = pd.DataFrame(RightWingBack[(RightWingBack['Club'] == tName1) | (RightWingBack['Club'] == tName2)])
teamDict[4] = rwb.to_dict('list')['Name']
#4 RWB
cm = pd.DataFrame(CentralMid[(CentralMid['Club'] == tName1) | (CentralMid['Club'] == tName2)])
teamDict[5] = cm.to_dict('list')['Name']
#5 CM
rm = pd.DataFrame(RightMid[(RightMid['Club'] == tName1) | (RightMid['Club'] == tName2)])
teamDict[6] = rm.to_dict('list')['Name']
#6 RM
lm = pd.DataFrame(LeftMid[(LeftMid['Club'] == tName1) | (LeftMid['Club'] == tName2)])
teamDict[7] = lm.to_dict('list')['Name']
#7 LM
st = pd.DataFrame(Striker[(Striker['Club'] == tName1) | (Striker['Club'] == tName2)])
teamDict[8] = st.to_dict('list')['Name']
#8 ST
lf = pd.DataFrame(LeftForward[(LeftForward['Club'] == tName1) | (LeftForward['Club'] == tName2)])
teamDict[9] = lf.to_dict('list')['Name']
#9 LF
rf = pd.DataFrame(RightForward[(RightForward['Club'] == tName1) | (RightForward['Club'] == tName2)])
teamDict[10] = rf.to_dict('list')['Name']
#10 RF

allstar = pd.DataFrame.from_dict(teamDict, orient = 'index')
allstar = allstar.transpose()

'''gka=np.array(teamDict['GK'])
lcda=np.array(teamDict['LCD'])
rcda=np.array(teamDict['RCD'])
lwba=np.array(teamDict['LWB'])
rwba=np.array(teamDict['RWB'])
cma=np.array(teamDict['CM'])
rma=np.array(teamDict['RM'])
lma=np.array(teamDict['LM'])
sta=np.array(teamDict['ST'])
lfa=np.array(teamDict['LF'])
rfa=np.array(teamDict['RF'])
'''

#print(teamDict[3][0])
#print(getOverall(teamDict,3,0))

# The indices for each team position
allstarTeamPositions = {
    'gk': gk,
    'lcd': lcd,
    'rcd': rcd,
    'lwb': lwb,
    'rwb': rwb,
    'cm': cm,
    'rm': rm,
    'lm': lm,
    'st': st,
    'lf': lf,
    'rf': rf
}

def getOverall(teamDict,i,j):
    '''
    Get fixed Overall score and position for the specified index in teamDict
    '''
    player_name = teamDict[i][j]
    pos = list(allstarTeamPositions.keys())[i]
    records = allstarTeamPositions[pos]
    player_overall = int(records[records.Name == player_name]['Overall'])
    return (pos, player_overall)

def getAllOverallsInPosition(teamDict, i):
    '''
    Get all overalls in position i in teamDict
    '''
    
    return (getOverall(teamDict,i,k)[1] for k in range(len(teamDict[i])))
    
def checkPossibility(teamDict,i,budget):
    '''
    Check if there's a feasible team in teamDict,
    given budget and starting at position i
    '''
    #import pdb;pdb.set_trace();
    b = budget
    nexti=i+1
    
    # All Overalls to consider for the next position
    overalls = getAllOverallsInPosition(teamDict, nexti)

    if nexti==10:
        # Return whether there's any player in our budget
        return any(o <= b for o in overalls)
    else:
        # Check if there's any possibility within all Overall scores that are in our budget
        return any(checkPossibility(teamDict, nexti, b - o) for o in overalls if o <= b)
                        
def optimalTeam(teamDict,budget):
    '''
    gk: Goalkeeper
    lcd: Left Central Defender
    rcd: Right Central Defender
    lwb: Left Wing Back
    rwb: Right Wing Back
    cm: Center Mid
    lm: Left Mid
    rm: Right Mid
    st: Striker
    lf: Left Forward
    rf: Right Forward
    '''

    b = budget   
    allstarTeam = {'gk':'','lcd':'','rcd':'','lwb':'','rwb':'','cm':'','rm':'','lm':'','st':'','lf':'','rf':''}
    for i in range(len(teamDict)):
        for j in range(len(teamDict[i])):
            pos, overall = getOverall(teamDict,i,j)    
            if overall <= b:
                if i==10 or checkPossibility(teamDict,i,b-overall):
                    b = b - overall
                    allstarTeam[pos] = teamDict[i][j]
                    break
    return allstarTeam

test=optimalTeam(teamDict,900)
#cp = checkPossibility(teamDict,1,800)
print (test)

                
                
            
    
    


