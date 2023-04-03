import pandas as pd
import pickle

# Load stat_df.pkl
with open('stat_df.pkl', 'rb') as f:
    stat_df = pickle.load(f)

print(stat_df)
# Calculate mean and standard deviation of columns quantity, exposure for each cluster in c6_labels