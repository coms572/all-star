from data import  positions, budget

# A* Search

def replaceNext(team, pos):
    '''
    replace the player in team at pos with the next most costly in teamDict.
    '''

    # TODO: pre-sort each position in teamDict by evaluation?
    
    name = team[pos]
    df = sorted_players[pos]
    player_idx = df.index[df.Name == name]
    if player_idx == df.shape[0] - 1:
        return None
   
    next_name = df.iloc[player_idx+1].Name.values[0]
    next_team = team.copy()
    next_team[pos] = next_name
    return next_team

from statistics import mean

def value(team):
    '''
    return the distance from the team cost to the budget,
    scaled by the team value.
    Between two teams with the same cost,
    the one with higher value should have a better evaluation.
    
    A better evaluation is LOWER. This is a minimization heuristic - minimize the distance from cost to budget.
    '''
    
    team_cost = cost(team)
    cost_difference = budget - team_cost
    if (cost_difference == 0):
        return 0
    
    weight = mean([all_players[all_players.Name == name].Evaluation.values[0] for name in team.values()])
    val = cost_difference * weight
    #val = sum([all_players[all_players.Name == name].Evaluation.values[0] for name in team.values()])
    
    return val

def isInBudget(team):
    '''
    return whether a given team fits the budget.
    '''
    return cost(team) <= budget

def cost(team):
    '''
    return the cost of a given team.
    '''
    
    sum = 0
    for pos, name in team.items():
        sum += all_players.loc[all_players.Name == name].Overall.values[0]
    
    return sum

import random

def succ(team):
    ret = []
    for pos in team:
        n = replaceNext(team, pos) # Maybe should replace from team
        if n is None or cost(n) > budget:
            continue

        if value(n) < value(team):
            ret.append(n)
        
    return random.choice(ret) if len(ret) > 0 else None

def localSearch(initial):
    current = initial
    count = 0
    while True:
        neighbor = succ(current)
        if neighbor is None:
            break
        
        if value(neighbor) > value(current):
            break
        else:
            count += 1
            current = neighbor

        
    print('%d iterations' % count)
    return current

def fancy_sort(df):
    '''
    Add h2 to df and sort df by h2.
    '''
    sorted_df = df[['Overall', 'NormalSkills', 'Skills', 'Name']].copy()
    sorted_df['Evaluation'] =  df['NormalSkills'] / df['Overall']
    sorted_df = sorted_df.sort_values(by='Evaluation', ascending = False)
    sorted_df = sorted_df.reset_index()
    return sorted_df

import pandas as pd

evaluationColumn = 'Evaluation'

sorted_players = { posName: fancy_sort(pos.df) for posName, pos in positions.items() }

all_dfs = [df for df in sorted_players.values()]
all_players = pd.concat(all_dfs)



# import seaborn as sns
# import matplotlib.pyplot as plt


# plt.figure(figsize=(10,6))
# sns.scatterplot(x='Overall', y='NormalSkills', data=all_players, color='orange')
# plt.show()


initial = { pos: df.iloc[0].Name for pos, df in sorted_players.items() }
# import random
# initial = { pos: random.choice(df.Name) for pos, df in sorted_players.items() }
init_cost = cost(initial)
print('min budget: %d' % init_cost)
if budget < init_cost:
    raise Exception('the budget must be greater than or equal to %d.' % init_cost)

import time
start_time = time.time()
t = localSearch(initial)
end_time = time.time()
print("Local search, budget %d: %s ms" % (budget, ((end_time - start_time) * 100)))

#print('initial: %s' % initial)
#print('goal:    %s' % t)
print('team value', value(t))
print('sum cost', cost(t))
print('sum skills', sum([all_players[all_players.Name == t[pos]].Skills.values[0] for pos in t]))
tval = value(initial)
