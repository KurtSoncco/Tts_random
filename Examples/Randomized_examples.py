import pandas as pd
import numpy as np

# Read the base CSV file
base_profile = pd.read_csv('Examples\Example_Profile.csv', header=None, names=['Depth', 'Vs'])

# Calculate the depth difference
depth_diff = base_profile['Depth'].diff().fillna(0)
base_profile['Thickness'] = depth_diff

# Define the number of profiles to generate
num_profiles = 10

# Define the minimum and maximum number of rows
min_rows = 3
max_rows = base_profile.shape[0] + 10

# Get the second maximum Vs value
second_max_Vs = base_profile['Vs'].nlargest(2).iloc[-1]

# Loop over the number of profiles
for i in range(num_profiles):
    # Generate a random number of rows
    num_rows = np.random.randint(min_rows, max_rows + 1)

    # Generate random variations of thickness and Vs values for the base profile
    thickness_variation = np.random.uniform(-0.1, 0.1, size=min(num_rows, base_profile.shape[0]))
    Vs_variation = np.random.uniform(-0.1, 0.1, size=min(num_rows, base_profile.shape[0]))

    # Adjust Vs_variation to not exceed the second maximum Vs value
    Vs_variation = np.where(base_profile['Vs'][:min(num_rows, base_profile.shape[0])] * (1 + Vs_variation) > second_max_Vs, second_max_Vs / base_profile['Vs'][:min(num_rows, base_profile.shape[0])] - 1, Vs_variation)

    # Create new profile with the base profile and random variations
    new_profile = pd.DataFrame({
        'Thickness': base_profile['Thickness'][:min(num_rows, base_profile.shape[0])] * (1 + thickness_variation),
        'Vs': base_profile['Vs'][:min(num_rows, base_profile.shape[0])] * (1 + Vs_variation)
    })

    # If num_rows is greater than the base profile, append additional rows with random values
    if num_rows > base_profile.shape[0]:
        additional_rows = pd.DataFrame({
            'Thickness': np.random.uniform(base_profile['Thickness'].min(), base_profile['Depth'].max(), size=num_rows - base_profile.shape[0]),
            'Vs': np.random.uniform(base_profile['Vs'].min(), second_max_Vs, size=num_rows - base_profile.shape[0])
        })
        new_profile = pd.concat([new_profile, additional_rows], ignore_index=True)
    # If num_rows is less than the base profile, drop the extra rows
    elif num_rows < base_profile.shape[0]:
        new_profile = new_profile.iloc[:num_rows]

    # Ensure the last row's second column value is a high value
    new_profile['Vs'].iloc[-1] = base_profile['Vs'].iloc[-1] * np.random.uniform(0.9, 1.1)

    # Calculate the depth
    new_profile['Depth'] = new_profile['Thickness'].cumsum()

    # Rearrange the order of the columns
    new_profile = new_profile[['Depth', 'Vs']]
    
    # Write the new profile to a new CSV file
    new_profile.to_csv(f'Examples\Randomized_Profile_{i+1}.csv', index=False, header=False)





