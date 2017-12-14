#ESM Log Pull/Graph
#Version 1.5 using matplotlib module
import matplotlib
matplotlib.use("TkAgg")
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
fig, (axes1, axes2) = plt.subplots(2, 2, figsize=(10, 10))

for i, (idx, row) in enumerate(df.set_index('Rule').iterrows()):
    ax1 = axes1[i // 2, i % 2]
    row = row[:2]
    row = row[row.gt(row.sum() * .01)]
    ax1.pie(row, labels=row.index, startangle=30)
    ax1.set_title(idx)


for i, (idx, row) in enumerate(df.set_index('Rule').iterrows()):
    ax2 = axes2[i // 2, i % 2]
    row = row[2:]
    row = row[row.gt(row.sum() * .01)]
    ax2.pie(row, labels = row.index, startangle = 30)
    ax2.set_title(idx)
    
fig.subplots_adjust(wspace = .2)

#Plot graph
plt.show()