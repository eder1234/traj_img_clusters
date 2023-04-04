import pandas as pd
import pickle

# Load stat_df.pkl
with open('stat_df.pkl', 'rb') as f:
    stat_df = pickle.load(f)

# Types of elements in stat_df['exposure']
exp_list = stat_df['exposure'].unique()

# Types of elements in stat_df['quantity']
qty_list = stat_df['quantity'].unique()

# Types of elements in stat_df['c6_labels']
c6_labels = stat_df['c6_labels'].unique()

mot_param = ['VCL', 'VAP', 'VSL', 'LIN', 'STR', 'WOB', 'BeatCross']#, 'ALH']

# Calculate mean and standard deviation of column VAP and WOB for each element in exp_list, qty_list and c6_labels
for exp in exp_list:
    for qty in qty_list:
        for c6 in c6_labels:
            for param in mot_param:
                print('exp =', exp, 'qty =', qty, 'c6 =', c6, 'param =', param)
                print('mean =', stat_df[(stat_df['exposure'] == exp) & (stat_df['quantity'] == qty) & (stat_df['c6_labels'] == c6)][param].mean())
                print('std =', stat_df[(stat_df['exposure'] == exp) & (stat_df['quantity'] == qty) & (stat_df['c6_labels'] == c6)][param].std())
                print()

print('Done')
