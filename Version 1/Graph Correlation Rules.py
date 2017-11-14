#ESM Log Pull/Graph
#Version 1.5 using matplotlib module

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Import .csv log from source folder, TBD by Consultant
#df = pd.read_csv('/Users/pcmaster/Documents/GitHub/ESM-Logs-Script/Correlation Rulesets/47-4000023.csv')
df = pd.read_csv('C:/Users/rgarbacz/Documents/GitHub/ESM-Logs-Script/Correlation Rulesets/47-4000116.csv')

#Plot from dataframe as bar graph with subplots for each statistic; X-Axis represents Ruleset and corresponding rules/triggers; change title to reflect which Ruleset is being shown
ax = df.plot(kind = 'bar', title = '47-4000116', subplots = True, sharex = 'True', figsize = (15,9), legend = True, fontsize = 12)

plt.xticks( np.arange(4) , ('Ruleset','Rule 1','Rule 2','Trigger 1'), rotation = 90)

#Plot graph
plt.show()
