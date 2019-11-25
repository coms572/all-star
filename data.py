import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data.csv")
#GoalKeeping Characteristics
'''
adding some other comment
May be applicable:
Stamina
Strength
Agility

Should keep all:
GKDiving
GKHandling
GKKicking
GKPositioning
GKReflexes
'''

def plot_stat(df, statname, axis_name=''):    
    '''
    Plot a stat for each player.
    '''

    plt.figure(figsize=(15,6))
    
    # Generate sequential data and plot
    sd = df.sort_values(statname, ascending=False)[:5]
    x1 = np.array(list(sd['Name']))
    y1 = np.array(list(sd[statname]))
    sns.barplot(x1, y1)
    plt.ylabel(axis_name if axis_name else statname)

def add_stat(df, statname, weights_by_prop):
    '''
    Add a stat to a dataframe by summing each prop, times its weight.
    '''
    
    df.insert(0, statname, 0)
    for prop in weights_by_prop:
        df[statname] += df[prop] * weights_by_prop[prop]
    
    return df

df = add_stat(df, 'gk_skills', dict(
        {
            'GKDiving': 0.6,
            'GKHandling': 0.8,
            'GKKicking': 0.8,
            'GKPositioning': 1.2,
            'GKReflexes': 0.9
        }))

df = add_stat(df, 'striker_skills', dict(
        {
            'Crossing': 0.6,
            'Finishing': 0.8,
            'HeadingAccuracy': 0.3,
            'ShortPassing': 0.7,
            'Dribbling': 0.6,
            'Curve': 0.3,
            'BallControl': 0.5,
            'Acceleration': 0.9,
            'Agility': 0.9,
            'Reactions': 0.8,
            'ShotPower': 0.6,
            'Stamina': 0.7,
        }))
    
plot_stat(df, 'striker_skills')
plot_stat(df, 'gk_skills')
    