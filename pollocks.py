import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import numpy as np
import pandas as pd
import pickle

# Load master_28062022.pkl

with open('C:\\Users\\ederro\\Documents\\GitHub\\objects\\master_df\\new_df.pkl', 'rb') as f:
    master_df = pickle.load(f)

# List of colors
colors_list = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

# Values in master_df['quantity']
target_cluster = ['c6_labels', 'c7_labels', 'c8_labels']
tc = 2 # This method can be easily improved...
quantity_list = master_df['quantity'].unique().tolist()
exposure_list = master_df['exposure'].unique().tolist()
cluster_list = master_df[target_cluster[tc]].unique().tolist()

# Create the figure
fig, ax = plt.subplots()

legend_list = []
for i in range(len(quantity_list)):
    legend_list.append(Line2D([0], [0], color=colors_list[i], lw=4, label=quantity_list[i]))

for cluster in cluster_list:
    print(cluster)
    for e in exposure_list:
        print(e)
        for index, row in master_df.iterrows():
            if (row['exposure'] == e) & (row[target_cluster[tc]] == cluster):        
                x = row['traj'][0]
                y = row['traj'][1]
                colors = quantity_list.index(row['quantity'])
                l = row['quantity']
                plt.plot(x, y, color=colors_list[colors])
        title = 'c_' + str(cluster) + '_' + 'e_' + str(e)
        print(title)
        plt.title(title)
        plt.legend(handles=legend_list, loc='upper left')
        filename = 'C:\\Users\\ederro\\Documents\\GitHub\\objects\\temp\\' + title + '.png'
        plt.savefig(filename) 
        plt.close("all")