#ESM Log Test
#Version 1.0 using Pandas

import plotly as ply
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
ply.tools.set_credentials_file(username = 'Resiliant', api_key = 'u0lOcoIq4BtzOIgeEfxW')

df = pd.read_csv('esm-log-test.csv')
sample_data_table = FF.create_table(df.head())
py.plot(sample_data_table, filename = 'ESM Log Test')

ax = df.plot(kind = 'bar', title = 'ESM Log Test', figsize = (8,4), legend = True, fontsize = 12)
ax.set_xlabel("Corr Rule", fontsize = 12)
ax.set_ylabel("Value", fontsize = 12)
plt.show()





#multiple_bars = plt.figure()

#x = [474000116,474000114,474000023,478000015]
#y = [1169956,29011690,18452063,25431003]
#z = [8143004,23796863,12433978,0]
#k = [12744,11848,10907,0]
#l = [1629,248138,160651,121189]

#ax = plt.subplot()
#ax.bar(x, y, width=1, color = 'b')
#ax.bar(x, z, width=1, color = 'g')
#ax.bar(x, k, width=1, color = 'r')
#ax.bar(x, l, width=1, color = 'c')

#plt.show()
#plot_url = py.plot_mpl(multiple_bars, filename='ESM Log to Graph Test')
