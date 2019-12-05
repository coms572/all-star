# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:49:45 2019
@author: bhatt
"""

from data import *

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

import random
import math

# Annealing Search

def replaceRandom(current, allPlayers):
    pos = random.choice(current.keys())
    current[pos] = random.choice(allPlayers[pos])

schedule = [n / 100 for n in range(0, 100)]
schedule.reverse()

def value(team, budget):
    '''
    return the distance from the team cost to the budget,
    scaled by the team value.
    Between two teams with the same cost,
    the one with higher value should have a higher evaluation.
    '''

    # TODO: Calculate it.

    pass

def aStarSearch(initial, teamDict, budget):

    # TODO: A star search

    return initial

def get_min_cost(teamDict, i):
    '''
    returns the name of the player in
    the position at index i who has the minimum cost.
    '''

    return ''

initial = { pos: get_min_cost(teamDict, i) for i, pos in enumerate(teamDict.keys()) }
# t = aStarSearch(initial, teamDict, 900)

test = optimalTeam(teamDict,900)
#cp = checkPossibility(teamDict,1,800)
print (test)

                
                
            
    
    


