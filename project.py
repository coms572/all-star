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
GoalKeeperSorted = df.sort_values('GoalKeeper', ascending=False)[:18207]


df['CentralDefender']=4*(df.Strength+df.Reactions+df.Crossing)+5*(df.Interceptions+df.SlidingTackle+df.StandingTackle) + 3*(df.Acceleration+df.SprintSpeed+df.ShotPower+df.LongShots)+2*(df.BallControl+df.Stamina+df.Jumping+df.FKAccuracy)+df.Aggression+df.Vision+df.ShortPassing+df.LongPassing
CentralDefender = df.sort_values('CentralDefender', ascending=False)[:18207]