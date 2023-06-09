import pandas as pd
import pickle

# Load stat_df.pkl
with open('stat_df.pkl', 'rb') as f:
    stat_df = pickle.load(f)
stat_df['ALH'][3538] = 2.7122898 # Error in the input master dataframe
stat_df['ALH'] = stat_df['ALH'].astype(float)

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

mot_param = ['VCL', 'VAP', 'VSL', 'LIN', 'STR', 'WOB', 'BeatCross', 'ALH']

print('num_c = 6')
# Calculate mean and standard error of mot_param for each element in exp_list, qty_list and c6_labels
for exp in exp_list:
    for qty in qty_list:
        for c6 in c6_labels:
            for param in mot_param:
                print('exp =', exp, 'qty =', qty, 'c6 =', c6, 'param =', param)
                describe = stat_df[(stat_df['exposure'] == exp) & (stat_df['quantity'] == qty) & (stat_df['c6_labels'] == c6)][param].describe()
                print(describe)
                print('Standard error =', describe['std']/describe['count']**0.5)
                print()


print('num_c = 7')
# Calculate mean and standard error of mot_param for each element in exp_list, qty_list and c7_labels
for exp in exp_list:
    for qty in qty_list:
        for c7 in c7_labels:
            for param in mot_param:
                print('exp =', exp, 'qty =', qty, 'c7 =', c7, 'param =', param)
                describe = stat_df[(stat_df['exposure'] == exp) & (stat_df['quantity'] == qty) & (stat_df['c7_labels'] == c7)][param].describe()
                print(describe)
                print('Standard error =', describe['std']/describe['count']**0.5)
                print()

print('num_c = 8')
# Calculate mean and standard error of mot_param for each element in exp_list, qty_list and c8_labels
for exp in exp_list:
    for qty in qty_list:
        for c8 in c8_labels:
            for param in mot_param:
                print('exp =', exp, 'qty =', qty, 'c8 =', c8, 'param =', param)
                describe = stat_df[(stat_df['exposure'] == exp) & (stat_df['quantity'] == qty) & (stat_df['c8_labels'] == c8)][param].describe()
                print(describe)
                print('Standard error =', describe['std']/describe['count']**0.5)
                print()


print('Done')
