# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:49:45 2019
@author: bhatt
"""

from data import teamDictH,teamDict, allstarTeamPositions, budget

def getCost(teamDict,i,j):
    '''
    Get cost and position for the player at the specified index in teamDict.
    We're currently using Overall score as the cost for each player.
    '''
    player_name = teamDict[i][j]
    pos = list(allstarTeamPositions.keys())[i]
    records = allstarTeamPositions[pos]
    player_cost = int(records[records.Name == player_name]['Overall'])
    return (pos, player_cost)

def getAllCostsInPosition(teamDict, i):
    '''
    Get all costs in position i in teamDict.
    '''
    
    return (getCost(teamDict,i,k)[1] for k in range(len(teamDict[i])))
    
def checkPossibility(teamDict,i,budget):
    '''
    Check if there's a feasible team in teamDict,
    given budget and starting at position i
    '''
    #import pdb;pdb.set_trace();
    b = budget
    nexti=i+1
    
    # All costs to consider for the next position
    costs = getAllCostsInPosition(teamDict, nexti)

    if nexti == len(teamDict) - 1:
        # Return whether there's any player in our budget
        return any(o <= b for o in costs)
    else:
        # Check if there's any possibility within all costs that are in our budget
        return any(checkPossibility(teamDict, nexti, b - o) for o in costs if o <= b)
                        
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
            pos, cost = getCost(teamDict,i,j)    
            if cost <= b:
                if i == len(teamDict) - 1 or checkPossibility(teamDict, i, b - cost):
                    b = b - cost
                    allstarTeam[pos] = teamDict[i][j]
                    break
    return allstarTeam

import time
start_time = time.time()
test = optimalTeam(teamDict,budget)
end_time = time.time()
print("Normal backtracking search, budget %d: %s ms" % (budget, ((end_time - start_time) * 1000)))
print('Skills: %d' % sum([allstarTeamPositions[pos][allstarTeamPositions[pos].Name == name].Skills.values[0] for pos, name in test.items()]))
print('Overall: %d' % sum([allstarTeamPositions[pos][allstarTeamPositions[pos].Name == name].Overall.values[0] for pos, name in test.items()]))
#test = optimalTeam(teamDict,900)
#test = optimalTeam(teamDictH,850)
#cp = checkPossibility(teamDict,1,800)
print (test)

                
                
            
    
    


