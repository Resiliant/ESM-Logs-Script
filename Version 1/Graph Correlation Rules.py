#ESM Log Pull/Graph
#Version 1.5 using matplotlib module

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#DEVELOPER NOTES:
#   Will need to explore method to show exact statistical values for each bar instead of determining value from yticks

#Import .csv log from source folder, TBD by Consultant; top path is MacOS, bottom path is Windows
df = pd.read_csv('/Users/pcmaster/Documents/GitHub/ESM-Logs-Script/Correlation Rulesets/47-4000116.csv')
#df = pd.read_csv('C:/Users/rgarbacz/Documents/GitHub/ESM-Logs-Script/Correlation Rulesets/47-4000116.csv')

#Plot from dataframe as bar graph with subplots for each statistic; X-Axis represents Ruleset and corresponding rules/triggers; change title to reflect which Ruleset is being shown
ax = df.plot(kind = 'bar', title = '47-4000116', subplots = True, sharex = 'True', figsize = (15,9), legend = True, fontsize = 12)
#Apply Labels to each column
plt.xticks( np.arange(4) , ('Ruleset','Rule 1','Rule 2','Trigger 1'), rotation = 0)

#Plot graph
plt.show()
