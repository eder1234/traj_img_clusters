import pandas as pd
import pickle

# Load master_280620222.pkl (currently stored in traj_SCAN folder)
with open('C:\\Users\\ederro\\Documents\\GitHub\\traj_SCAN\\master_28062022.pkl', 'rb') as f:
    master_df = pickle.load(f)

master_df = master_df[:20500]

with open('df.pkl', 'rb') as f:
    clusters_df = pickle.load(f)

full_df = pd.concat([master_df, clusters_df], axis=1)

stat_df = full_df.drop(['traj', 'img'], axis=1)
stat_df.to_pickle('stat_df.pkl')
print(stat_df)
