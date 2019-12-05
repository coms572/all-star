from data import positions

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
    team[pos] = next_name
    return team

from statistics import mean

def value(team):
    '''
    return the distance from the team cost to the budget,
    scaled by the team value.
    Between two teams with the same cost,
    the one with higher value should have a higher evaluation.
    '''
    
    team_cost = cost(team)
    cost_difference = budget - team_cost
    if (cost_difference == 0):
        return 0
    
    weight = mean([all_players[all_players.Name == name][evaluationColumn].values[0] for name in team.values()])
    val = cost_difference * weight
    
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

def succ(team):
    best = team
    for pos in team:
        n = replaceNext(team, pos)
        if n is None or cost(n) > budget:
            continue

        if value(n) > value(best):
            best = n
        
    return best

def localSearch(initial):
    current = initial
    while True:
        neighbor = succ(current)
        if neighbor is None:
            break
        
        if value(neighbor) <= value(current):
            return current
        else:
            current = neighbor

def fancy_sort(df):
    '''
    Add h2 to df and sort df by h2.
    '''
    sorted_df = df[[evaluationColumn, 'Overall', 'Name']].copy()
    # sorted_df['Evaluation'] =  df['Skills'] / df['Overall']
    sorted_df.sort_values(by=evaluationColumn)
    sorted_df = sorted_df.reset_index()
    return sorted_df

import pandas as pd

budget = 900
evaluationColumn = 'PlayerHeuristic'

sorted_players = { posName: fancy_sort(pos.df) for posName, pos in positions.items() }
all_dfs = [df for df in sorted_players.values()]
all_players = pd.concat(all_dfs)

initial = { pos: df[df[evaluationColumn] == df[evaluationColumn].max()].Name.values[0] for pos, df in sorted_players.items() }
t = localSearch(initial)
print('team value', value(t))
print('sum cost', cost(t))

def get_skills(pos):
    h = all_players[all_players.Name == t[pos]][evaluationColumn].values[0]
    overall = all_players[all_players.Name == t[pos]]['Overall'].values[0]
    return h * overall
print('sum skills', sum([get_skills(pos) for pos in t]))
tval = value(initial)
