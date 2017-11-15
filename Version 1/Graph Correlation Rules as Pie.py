# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:37:26 2017

@author: rgarbacz
"""

#ESM Correlation Rule Graph as pie chart

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Import .csv log from source folder, TBD by Consultant; top path is MacOS, bottom path is Windows
#df = pd.read_csv('/Users/pcmaster/Documents/GitHub/ESM-Logs-Script/Correlation Rulesets/47-4000023.csv')
df = pd.read_csv('C:/Users/rgarbacz/Documents/GitHub/ESM-Logs-Script/Correlation Rulesets/47-4000116.csv')

#labels = [r'Ruleset', r'Rule 1', r'Rule 2', r'Trigger 1']

#Plot from dataframe as bar graph with subplots for each statistic; X-Axis represents Ruleset and corresponding rules/triggers; change title to reflect which Ruleset is being shown
#ax = df.plot(kind = 'pie', title = '47-4000116', subplots = True, figsize = (18,9), legend = True, fontsize = 12)
#plt.legend(labels, loc="best")
#plt.axis('equal')

#df = pd.DataFrame(3 * np.random.rand(4, 4), index=['a', 'b', 'c', 'd'], 
#                  columns=['x', 'y','z','w'])

plt.style.use('ggplot')
colors = plt.rcParams['axes.color_cycle']
values = df['Ruleset']

fig, axes = plt.subplots(nrows=2, ncols=2)
for ax, col in zip(axes.flat, df.columns):
    ax.pie(df[col], labels=df.index, autopct= '%.02f', colors=colors)
    ax.set(ylabel='', title=col, aspect='equal')

axes[0, 0].legend(bbox_to_anchor=(0, 0.5))




#  




#Plot graph
plt.show()