#ESM Log Pull/Graph
#Version 1.0 using matplotlib module

import matplotlib.pyplot as plt
import plotly.plotly
plotly.tools.set_credentials_file(username = 'Resiliant', api_key = 'u0lOcoIq4BtzOIgeEfxW')
#import numpy as np

#[w,x,y,z] = np.loadtxt('esm-log-test.csv', delimiter=',', unpack=True)
#plt.bar(x, label='ESM Log Data', color='g')
#plt.legend()
#plt.xlabel('x axis')
#plt.ylabel('y axis')
#plt.title('ESM Log Test')
#plt.show()

multiple_bars = plt.figure()

x = [474000116,474000114,474000023,478000015]
y = [1169956,29011690,18452063,25431003]
z = [8143004,23796863,12433978,0]
k = [12744,11848,10907,0]
#l = [1629,248138,160651,121189]

ax = plt.subplot()
ax.bar(x, y, width=1, color = 'b')
ax.bar(x, z, width=1, color = 'g')
ax.bar(x, k, width=1, color = 'r')
#ax.bar(x, l, width=1, color = 'c')

plt.show()
plot_url = py.plot_mpl(multiple_bars, filename='ESM Log to Graph Test')
