from data import teamDict, allstarTeamPositions
from data import df as full_df

# A* Search

def replaceNext(team, teamDict, pos):
    '''
    replace the player in team at pos with the next most costly in teamDict.
    '''

    # TODO: pre-sort each position in teamDict by cost?
    
    next = None
    pos = i_to_pos(pos)
    pos_players = allstarTeamPositions[pos]
    players = pos_players.loc[:, ['Name', 'Overall']].sort_values('Overall', ascending = True)
    players.reset_index(inplace = True)
    for i, p in players.iterrows():
        if i == len(players) - 1:
            return None
        if p.Name == team[pos]:
            next = players.iloc[[i + 1]]
            
    if next is None:
        return None
    else:
        team[pos] = next
        return team

def value(team, budget):
    '''
    return the distance from the team cost to the budget,
    scaled by the team value.
    Between two teams with the same cost,
    the one with higher value should have a higher evaluation.
    '''
    
    val = budget - cost(team)
    
    return val if val > 0 else 0

def isInBudget(team, budget):
    '''
    return whether a given team fits the budget.
    '''
    return cost(team) <= budget

def cost(team):
    '''
    return the cost of a given team.
    '''
    
    sum = 0
    for pos, player in team:
        sum += full_df.loc[full_df.Name == team].Overall
    
    return sum

def localSearch(initial, teamDict, budget):

initialPlayer = None
initialPos = 0
t = aStarSearch(initial, teamDict, 900)
