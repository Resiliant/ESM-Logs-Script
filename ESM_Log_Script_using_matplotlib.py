#ESM Log Pull/Graph
#Version 1.0 using matplotlib module

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np

#Create headers
#headers = ['Matches', 'Firings', 'Retention', 'Time Spent']
#Import .csv log from source folder, TBD by Consultant
df = pd.read_csv('/Users/pcmaster/Documents/GitHub/ESM-Logs-Script/Correlation Rulesets/47-4000023.csv')
#Plot from dataframe as bar graph with subplots for each statistic; X-Axis represents Ruleset and corresponding rules/triggers; change title to reflect which Ruleset is being shown
ax = df.plot(kind = 'bar', title = '47-4000116', subplots = True, sharex = 'True', figsize = (15,9), legend = True, fontsize = 12)
#Plot graph
plt.show()
