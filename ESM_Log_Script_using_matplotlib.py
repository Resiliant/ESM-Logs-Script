#ESM Log Pull/Graph
#Version 1.0 using matplotlib module

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np

#Create headers
headers = ['Matches', 'Firings', 'Retention', 'Time Spent']
#Import .csv log from source folder
df = pd.read_csv('esm-log-test.csv')
#Plot from dataframe as bar graph with subplots for each statistic; X-Axis represents a rule
ax = df.plot(kind = 'bar', title = 'Test', subplots = True, sharex = 'True', figsize = (15,9), legend = True, fontsize = 12)
#Plot graph
plt.show()
