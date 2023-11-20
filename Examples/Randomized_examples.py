import pandas as pd
import numpy as np

# Read the base CSV file
base_profile = pd.read_csv('Code\Example_Profile.csv', header=None, names=['Depth', 'Vs'])

# Define the number of profiles to generate
num_profiles = 10

# Define the minimum and maximum number of rows
min_rows = 2
max_rows = base_profile.shape[0] + 10

# Loop over the number of profiles
for i in range(num_profiles):
    # Generate a random number of rows
    num_rows = np.random.randint(min_rows, max_rows + 1)
    
    # Generate random variations of depth and Vs values for the base profile
    depth_variation = np.random.uniform(-0.1, 0.1, size=min(num_rows, base_profile.shape[0]))
    Vs_variation = np.random.uniform(-0.1, 0.1, size=min(num_rows, base_profile.shape[0]))

    # Create new profile with the base profile and random variations
    new_profile = pd.DataFrame({
        'Depth': base_profile['Depth'][:min(num_rows, base_profile.shape[0])] * (1 + depth_variation),
        'Vs': base_profile['Vs'][:min(num_rows, base_profile.shape[0])] * (1 + Vs_variation)
    })

    # If num_rows is greater than the base profile, append additional rows with random values
    if num_rows > base_profile.shape[0]:
        additional_rows = pd.DataFrame({
            'Depth': np.random.uniform(base_profile['Depth'].min(), base_profile['Depth'].max(), size=num_rows - base_profile.shape[0]),
            'Vs': np.random.uniform(base_profile['Vs'].min(), base_profile['Vs'].max(), size=num_rows - base_profile.shape[0])
        })
        new_profile = pd.concat([new_profile, additional_rows], ignore_index=True)
    # If num_rows is less than the base profile, drop the extra rows
    elif num_rows < base_profile.shape[0]:
        new_profile = new_profile.iloc[:num_rows]


    
    # Write the new profile to a new CSV file
    new_profile.to_csv(f'Examples\Randomized_Profile_{i+1}.csv', index=False, header=False)