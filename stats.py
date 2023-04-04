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

# Types of elements in stat_df['c7_labels']
c7_labels = stat_df['c7_labels'].unique()

# Types of elements in stat_df['c8_labels']
c8_labels = stat_df['c8_labels'].unique()

c_list = [c6_labels, c7_labels, c8_labels] # implement later

mot_param = ['VCL', 'VAP', 'VSL', 'LIN', 'STR', 'WOB', 'BeatCross']#, 'ALH']

print('num_c = 6')
# Calculate mean and standard deviation of mot_param for each element in exp_list, qty_list and c6_labels
for exp in exp_list:
    for qty in qty_list:
        for c6 in c6_labels:
            for param in mot_param:
                print('exp =', exp, 'qty =', qty, 'c6 =', c6, 'param =', param)
                print('mean =', stat_df[(stat_df['exposure'] == exp) & (stat_df['quantity'] == qty) & (stat_df['c6_labels'] == c6)][param].mean())
                print('std =', stat_df[(stat_df['exposure'] == exp) & (stat_df['quantity'] == qty) & (stat_df['c6_labels'] == c6)][param].std())
                print()

print('num_c = 7')
# Calculate mean and standard deviation of mot_param for each element in exp_list, qty_list and c7_labels
for exp in exp_list:
    for qty in qty_list:
        for c7 in c7_labels:
            for param in mot_param:
                print('exp =', exp, 'qty =', qty, 'c7 =', c7, 'param =', param)
                print('mean =', stat_df[(stat_df['exposure'] == exp) & (stat_df['quantity'] == qty) & (stat_df['c6_labels'] == c7)][param].mean())
                print('std =', stat_df[(stat_df['exposure'] == exp) & (stat_df['quantity'] == qty) & (stat_df['c6_labels'] == c7)][param].std())
                print()

print('num_c = 8')
# Calculate mean and standard deviation of mot_param for each element in exp_list, qty_list and c8_labels
for exp in exp_list:
    for qty in qty_list:
        for c8 in c8_labels:
            for param in mot_param:
                print('exp =', exp, 'qty =', qty, 'c8 =', c8, 'param =', param)
                print('mean =', stat_df[(stat_df['exposure'] == exp) & (stat_df['quantity'] == qty) & (stat_df['c6_labels'] == c8)][param].mean())
                print('std =', stat_df[(stat_df['exposure'] == exp) & (stat_df['quantity'] == qty) & (stat_df['c6_labels'] == c8)][param].std())
                print()

print('Done')
