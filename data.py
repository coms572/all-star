import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data.csv")
print(df.head(7))

#GoalKeeping Characteristics
'''
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

a = 0.5
b = 1
c= 2
d = 3

df['gk_skills'] = (
        df.Stamina +
        df.Strength +
        df.Agility +
        df.GKDiving +
        df.GKHandling +
        df.GKKicking +
        df.GKPositioning +
        df.GKReflexes
        ) / 8
        
plt.figure(figsize=(15,6))
 
# Generate sequential data and plot
sd = df.sort_values('gk_skills', ascending=False)[:5]
x1 = np.array(list(sd['Name']))
y1 = np.array(list(sd['gk_skills']))
sns.barplot(x1, y1)
plt.ylabel("GK skills")
