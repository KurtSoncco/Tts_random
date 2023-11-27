# Start putting all the randomized profiles to the code

from Code import Travel_time
import pandas as pd
import os
import numpy as np

# Specify the folder path
folder_path = "Examples"

# Create a list of all csv files in the folder
csv_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.csv')]

# Input those files into Code
for i in csv_files:
    mat = pd.read_csv(f"Examples\{i}",header=None, names=['Depth','Vs'])
    Depth = mat['Depth'].values.reshape(-1)
    Vs = mat['Vs'].values.reshape(-1)
    Vs_all, depth_all, tts_all, base_tts = Travel_time(Vs, Depth)
