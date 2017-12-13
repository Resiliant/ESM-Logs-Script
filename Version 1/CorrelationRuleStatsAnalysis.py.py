#ESM Log Pull/Graph
#Version 1.5 using matplotlib module
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from tkinter import filedialog
from tkinter import *

# Get current python script directory
# ATTENTION: Need to standardize location of source data (csv files)
dir_path = os.path.dirname(os.path.realpath(__file__))
higherdir_path = os.path.dirname(dir_path)

# Prompt user for source log file location
root = Tk()
root.withdraw()
root.filename =  filedialog.askopenfilename(initialdir = dir_path,title = "Select Source File",filetypes = (("CSV (Comma Separated Values)","*.csv"),("All Files","*.*")))

# Read source log data into data frame
df = pd.read_csv(root.filename)
#Plot from dataframe as bar graph with subplots for each statistic; X-Axis represents Ruleset and corresponding rules/triggers; change title to reflect which Ruleset is being shown
ax = df.plot(kind = 'pie', title = '47-4000116', subplots = True, sharex = 'True', legend = True, fontsize = 12) #, figsize = (15,9)
#Apply Labels to each column
plt.xticks( np.arange(4) , ('Ruleset','Rule 1','Rule 2','Trigger 1'), rotation = 0)
#Plot graph
plt.show()



# #DEVELOPER NOTES:
# #   Will need to explore method to show exact statistical values for each bar instead of determining value from yticks
#
# #Import .csv log from source folder, TBD by Consultant; top path is MacOS, bottom path is Windows
# #df = pd.read_csv('/Users/pcmaster/Documents/GitHub/ESM-Logs-Script/Correlation Rulesets/47-4000023.csv')
# #df = pd.read_csv('/mnt/c/Users/melendez/Downloads/ESM-Logs-Script-master/ESM-Logs-Script-master/Correlation Rulesets/47-4000116.csv')
# df = pd.read_csv(higherdir_path+'/Correlation Rulesets/47-4000116.csv')
#
#
# #Plot from dataframe as bar graph with subplots for each statistic; X-Axis represents Ruleset and corresponding rules/triggers; change title to reflect which Ruleset is being shown
# ax = df.plot(kind = 'pie', title = '47-4000116', subplots = True, sharex = 'True', legend = True, fontsize = 12) #, figsize = (15,9)
# #Apply Labels to each column
# plt.xticks( np.arange(4) , ('Ruleset','Rule 1','Rule 2','Trigger 1'), rotation = 0)
#
# #Plot graph
# plt.show()
