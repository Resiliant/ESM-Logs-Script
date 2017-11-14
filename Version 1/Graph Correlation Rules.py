#ESM Log Pull/Graph
#Version 1.5 using matplotlib module

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
#import numpy as np

#Import .csv log from source folder, TBD by Consultant
#df = pd.read_csv('/Users/pcmaster/Documents/GitHub/ESM-Logs-Script/Correlation Rulesets/47-4000023.csv')
df = pd.read_csv('C:/Users/rgarbacz/Documents/GitHub/ESM-Logs-Script/Correlation Rulesets/47-4000116.csv')
#Plot from dataframe as bar graph with subplots for each statistic; X-Axis represents Ruleset and corresponding rules/triggers; change title to reflect which Ruleset is being shown
ax = df.plot(kind = 'bar', title = '47-4000116', subplots = True, sharex = 'True', figsize = (15,9), legend = True, fontsize = 12)

#for idx, label in enumerate(list(df.index)):
#	for acc in df.columns:
#		value = np.round(df.ix[idx][acc], decimals = 2)
#		ax.annotate(value, (idx,value), xytext = (0, 15), textcoords = 'offset points')

#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

#Plot graph
plt.show()
