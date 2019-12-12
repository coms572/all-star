#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:43:09 2019

@author: rishabhbhatt
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:49:45 2019
@author: bhatt
"""

from data import teamDictH, allstarTeamPositions, budget

def getCost(teamDictH,i,j):
    '''
    Get cost and position for the player at the specified index in teamDictH.
    We're currently using Overall score as the cost for each player.
    '''
    player_name = teamDictH[i][j]
    pos = list(allstarTeamPositions.keys())[i]
    records = allstarTeamPositions[pos]
    player_cost = int(records[records.Name == player_name]['Overall'])
    return (pos, player_cost)

def getAllCostsInPosition(teamDictH, i):
    '''
    Get all costs in position i in teamDictH.
    '''
    
    return (getCost(teamDictH,i,k)[1] for k in range(len(teamDictH[i])))
    
def checkPossibility(teamDictH,i,budget):
    '''
    Check if there's a feasible team in teamDictH,
    given budget and starting at position i
    '''
    #import pdb;pdb.set_trace();
    b = budget
    nexti=i+1
    
    # All costs to consider for the next position
    costs = getAllCostsInPosition(teamDictH, nexti)

    if nexti == len(teamDictH) - 1:
        # Return whether there's any player in our budget
        return any(o <= b for o in costs)
    else:
        # Check if there's any possibility within all costs that are in our budget
        return any(checkPossibility(teamDictH, nexti, b - o) for o in costs if o <= b)
                        
def optimalTeam(teamDictH,budget):
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
    for i in range(len(teamDictH)):
        for j in range(len(teamDictH[i])):
            pos, cost = getCost(teamDictH,i,j)    
            if cost <= b:
                if i == len(teamDictH) - 1 or checkPossibility(teamDictH, i, b - cost):
                    b = b - cost
                    allstarTeam[pos] = teamDictH[i][j]
                    break
    return allstarTeam

import time
start_time = time.time()
test = optimalTeam(teamDictH, budget)
end_time = time.time()
print("H backtracking search, budget %d: %s ms" % (budget, ((end_time - start_time) * 100)))
#cp = checkPossibility(teamDictH,1,800)
# print (test)
print('Overall: %d' % sum([allstarTeamPositions[pos][allstarTeamPositions[pos].Name == name].Overall.values[0] for pos, name in test.items()]))
print('Skills: %d' % sum([allstarTeamPositions[pos][allstarTeamPositions[pos].Name == name].Skills.values[0] for pos, name in test.items()]))
