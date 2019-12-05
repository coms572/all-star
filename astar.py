from data import teamDict, allstarTeamPositions

# A* Search

def replaceNext(team, teamDict, pos):
    '''
    replace the player in team at pos with the next most costly in teamDict.
    '''

    # TODO: pre-sort each position in teamDict by cost?
    
    pos = i_to_pos(pos)
    pos_players = allstarTeamPositions[pos]
    players = pos_players.loc[:, ['Name', 'Overall']].sort_values('Overall', ascending = True)
    players.reset_index(inplace = True)
    for i, p in players.iterrows():
        if i == len(players) - 1:
            return None
        if p.Name == team[pos]:
            return players.iloc[i + 1]
    
    return None

def value(team, budget):
    '''
    return the distance from the team cost to the budget,
    scaled by the team value.
    Between two teams with the same cost,
    the one with higher value should have a higher evaluation.
    '''

    # TODO: Calculate it.

    pass

def isInBudget(team, budget):
    '''
    return whether a given team fits the budget.
    '''
    pass

def cost(team):
    '''
    return the cost of a given team.
    '''
    pass

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, team=None):
        self.parent = parent
        self.team = team

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.team == other.team

def aStarSearch(initial, teamDict, budget):# Create start and end node
    start_node = Node(None, initial)
    start_node.g = start_node.h = start_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    current_node = None

    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # add current to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Generate children - advance one more person in the cost ordering for each position
        fringe = []
        for pos in teamDict.keys():

            # Get team of next node
            next_team = replaceNext(current_node.team, teamDict, pos)
            if next_team is None:
                continue

            # Make sure within range
            if isInBudget(next_team, budget):
                continue

            # Create new node
            new_node = Node(current_node, next_team)

            # Append
            fringe.append(new_node)

        # Loop through children
        for new_node in fringe:

            # Child is on the closed list
            for item in closed_list:
                if new_node == item:
                    continue

            # Create the f, g, and h values
            new_node.g = cost(new_node.team)
            new_node.h = value(new_node.team, budget)
            new_node.f = new_node.g + new_node.h

            # Child is already in the open list
            for open_node in open_list:
                if new_node == open_node and new_node.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(new_node)

    return current_node.team

def i_to_pos(i):
    return list(allstarTeamPositions.keys())[i]

def get_min_cost(teamDict, i):
    '''
    returns the name of the player in
    a given list of names has the minimum cost.
    '''
    
    df = allstarTeamPositions[i_to_pos(i)]

    return df.loc[df['Overall'].idxmin()].Name

initial = { i_to_pos(i): get_min_cost(teamDict, i) for i in teamDict.keys() }
t = aStarSearch(initial, teamDict, 900)