import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
# import numpy as np

dataset = pd.read_csv("data.csv") #Do not spoil this dataset
df=dataset
budget = 900

def compare_cost_measures():
    graph_df = pd.DataFrame(df[['Overall']])
    def m(s):
        s = s.replace('r(€|K|M)', '')
        if len(s) < 3:
            return 0
        return math.floor(float(s[1:-1]))
    graph_df['ValueInt'] = df[['Value']].applymap(m)
    graph_df['WageInt'] = df[['Wage']].applymap(m)
    
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='Overall', y='WageInt', data=graph_df, color='orange', alpha=0.2)
    # fig, ax = plt.subplots()
    # ax = sns.scatterplot(x='Overall', y='ValueInt', data=graph_df, ax=ax, color='teal', alpha=0.2)
    # ax2 = ax.twinx()
    # ax2.spines['left'].set_color('teal')
    # ax2.spines['right'].set_color('orange')
    # sns.scatterplot(x='Overall', y='WageInt', data=graph_df, ax=ax2, color='orange', alpha=0.2)
    plt.show()
    
# compare_cost_measures()

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

GoalKeeper['PlayerHeuristic']= GoalKeeper.GoalKeeper/GoalKeeper.Overall
GoalKeeper_h=GoalKeeper.sort_values('PlayerHeuristic', ascending=False)[:18207]

CentralMid['PlayerHeuristic']= CentralMid.CentralMid/CentralMid.Overall
CentralMid_h=CentralMid.sort_values('PlayerHeuristic', ascending=False)[:18207]

LeftCentralDefender['PlayerHeuristic']= LeftCentralDefender.CentralDefender/LeftCentralDefender.Overall
LeftCentralDefender_h=LeftCentralDefender.sort_values('PlayerHeuristic', ascending=False)[:18207]

LeftForward['PlayerHeuristic']= LeftForward.WingForward/LeftForward.Overall
LeftForward_h=LeftForward.sort_values('PlayerHeuristic', ascending=False)[:18207]

LeftMid['PlayerHeuristic']= LeftMid.LeftMid/LeftMid.Overall
LeftMid_h=LeftMid.sort_values('PlayerHeuristic', ascending=False)[:18207]

LeftWingBack['PlayerHeuristic']= LeftWingBack.WingBack/LeftWingBack.Overall
LeftWingBack_h=LeftWingBack.sort_values('PlayerHeuristic', ascending=False)[:18207]

RightCentralDefender['PlayerHeuristic']= RightCentralDefender.CentralDefender/RightCentralDefender.Overall
RightCentralDefender_h=RightCentralDefender.sort_values('PlayerHeuristic', ascending=False)[:18207]

RightForward['PlayerHeuristic']= RightForward.WingForward/RightForward.Overall
RightForward_h=RightForward.sort_values('PlayerHeuristic', ascending=False)[:18207]

RightMid['PlayerHeuristic']= RightMid.RightMid/RightMid.Overall
RightMid_h=RightMid.sort_values('PlayerHeuristic', ascending=False)[:18207]

RightWingBack['PlayerHeuristic']= RightWingBack.WingBack/RightWingBack.Overall
RightWingBack_h=RightWingBack.sort_values('PlayerHeuristic', ascending=False)[:18207]

Striker['PlayerHeuristic']= Striker.Striker/Striker.Overall
Striker_h=Striker.sort_values('PlayerHeuristic', ascending=False)[:18207]
#Number of players:
tName1 = 'Real Madrid'
tName2 = 'FC Barcelona'
team1 = pd.DataFrame(df[(df['Club'] == tName1)])
team2 = pd.DataFrame(df[(df['Club'] == tName2)])
teamDict = {}
teamDictH = {}
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

#for heuritic dictionary
gkh = pd.DataFrame(GoalKeeper_h[(GoalKeeper_h['Club'] == tName1) | (GoalKeeper_h['Club'] == tName2)])
teamDictH[0] = gkh.to_dict('list')['Name']
#0 GoalKeeper
lcdh = pd.DataFrame(LeftCentralDefender_h[(LeftCentralDefender_h['Club'] == tName1) | (LeftCentralDefender_h['Club'] == tName2)])
teamDictH[1] = lcdh.to_dict('list')['Name']
#1 LCD
rcdh = pd.DataFrame(RightCentralDefender_h[(RightCentralDefender_h['Club'] == tName1) | (RightCentralDefender_h['Club'] == tName2)])
teamDictH[2] = rcdh.to_dict('list')['Name']
#2 RCD
lwbh = pd.DataFrame(LeftWingBack_h[(LeftWingBack_h['Club'] == tName1) | (LeftWingBack_h['Club'] == tName2)])
teamDictH[3] = lwbh.to_dict('list')['Name']
#3 LWB
rwbh = pd.DataFrame(RightWingBack_h[(RightWingBack_h['Club'] == tName1) | (RightWingBack_h['Club'] == tName2)])
teamDictH[4] = rwbh.to_dict('list')['Name']
#4 RWB
cmh = pd.DataFrame(CentralMid_h[(CentralMid_h['Club'] == tName1) | (CentralMid_h['Club'] == tName2)])
teamDictH[5] = cmh.to_dict('list')['Name']
#5 CM
rmh = pd.DataFrame(RightMid_h[(RightMid_h['Club'] == tName1) | (RightMid_h['Club'] == tName2)])
teamDictH[6] = rmh.to_dict('list')['Name']
#6 RM
lmh = pd.DataFrame(LeftMid_h[(LeftMid_h['Club'] == tName1) | (LeftMid_h['Club'] == tName2)])
teamDictH[7] = lmh.to_dict('list')['Name']
#7 LM
sth = pd.DataFrame(Striker_h[(Striker_h['Club'] == tName1) | (Striker_h['Club'] == tName2)])
teamDictH[8] = sth.to_dict('list')['Name']
#8 ST
lfh = pd.DataFrame(LeftForward_h[(LeftForward_h['Club'] == tName1) | (LeftForward_h['Club'] == tName2)])
teamDictH[9] = lfh.to_dict('list')['Name']
#9 LF
rfh = pd.DataFrame(RightForward_h[(RightForward_h['Club'] == tName1) | (RightForward_h['Club'] == tName2)])
teamDictH[10] = rfh.to_dict('list')['Name']
#10 RF

# Organize positions

from collections import namedtuple
PositionRef = namedtuple('PositionRef', ['df', 'name', 'skills_name', 'index'])

positions = {
    'gk': PositionRef(name='gk', df=gk, skills_name='GoalKeeper', index=0),
    'lcd': PositionRef(name='lcd', df=lcd, skills_name='CentralDefender', index=1),
    'rcd': PositionRef(name='rcd', df=rcd, skills_name='CentralDefender', index=2),
    'lwb': PositionRef(name='lwb', df=lwb, skills_name='WingBack', index=3),
    'rwb': PositionRef(name='rwb', df=rwb, skills_name='WingBack', index=4),
    'cm': PositionRef(name='cm', df=cm, skills_name='CentralMid', index=5),
    'rm': PositionRef(name='rm', df=rm, skills_name='RightMid', index=6),
    'lm': PositionRef(name='lm', df=lm, skills_name='LeftMid', index=7),
    'st': PositionRef(name='st', df=st, skills_name='Striker', index=8),
    'lf': PositionRef(name='lf', df=lf, skills_name='WingForward', index=9),
    'rf': PositionRef(name='rf', df=rf, skills_name='WingForward', index=10),
}

# Check budget

min_team_cost = sum([df[df.Overall == df.Overall.min()].Overall.values[0] for pos in positions.keys()])
if budget < min_team_cost:
    raise Exception('the budget must be greater than or equal to %d.' % min_team_cost)

# Normalize skills

def add_normal_skill(df, specialSkillName):
    df['Skills'] = df[specialSkillName]
    df['NormalSkills'] = df['Skills'] / df['Skills'].max() * 100

for pos in positions.keys():
    add_normal_skill(positions[pos].df, positions[pos].skills_name)

for pos in positions.keys():
    add_normal_skill(df, positions[pos].skills_name)

# Graph player heuristic
def graph_h():
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='Overall', y='Skills', data=df, color='olive')
    plt.show()
#graph_h()

# Final df's

allstar = pd.DataFrame.from_dict(teamDict, orient = 'index')
allstar = allstar.transpose()


allstarH = pd.DataFrame.from_dict(teamDictH, orient = 'index')
allstarH = allstarH.transpose()

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
#print(getCost(teamDict,3,0))

# Backtracking

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