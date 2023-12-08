# Import necessary libraries
import pandas as pd
import os
from Code import Travel_time
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of the plots
sns.set_theme(style='ticks', font_scale=1.5)

# Get a list of all CSV files in the "examples" folder
# os.listdir() returns a list of all files in the specified directory
# The list comprehension filters this list to include only files that end with '.csv'
csv_files = [f for f in os.listdir('C:/Users/kurt-/Desktop/UC Berkeley/Fall 2023/Hallal/Travel Time Randomization/Python/Tts_random/Examples') if f.endswith('.csv')]

# Create a dictionary to hold the dataframes
# Each key-value pair will be the filename (without extension) and the corresponding dataframe
dataframes = {}

# Read each CSV file into a pandas DataFrame
for csv_file in csv_files:
    # The key is the filename without the extension
    # os.path.splitext() splits the filename into a tuple (root, ext), root is the filename without the extension
    key = os.path.splitext(csv_file)[0]
    # pd.read_csv() reads the csv file into a DataFrame
    # os.path.join() constructs a full file path to pass to pd.read_csv()
    dataframes[key] = pd.read_csv(os.path.join('C:/Users/kurt-/Desktop/UC Berkeley/Fall 2023/Hallal/Travel Time Randomization/Python/Tts_random/Examples', csv_file),
                                    header=None)

# Plot each Vs profile
# Loop over the keys in the dataframes dictionary (i.e., the filenames)
for i in dataframes.keys():
    data = dataframes[i]
    Vs = data.iloc[:, 1].values
    Depth = data.iloc[:, 0].values
    plt.step(Vs, Depth, label=i, where='pre')

plt.title('Vs Profiles')
plt.ylabel('Depth (m)')
plt.xlabel('Vs (m/s)')
plt.legend(fontsize=9.5)
plt.xlim(0, 2500)
plt.ylim(ymin=0)
# Get the current Axes object and invert the y-axis
ax = plt.gca()
ax.invert_yaxis()
# Put horizontal ticks on the top
ax.xaxis.tick_top()
# Put horizontal title on the top
ax.xaxis.set_label_position('top')
# Save the figure
plt.savefig('Examples/Randomized_Profiles.png', dpi=300, bbox_inches='tight')
plt.show()


# Initialize an empty dicttionary to hold the results
results = {}
for i in dataframes.keys():
    data = dataframes[i]
    Vs = data.iloc[:, 1].values
    Depth = data.iloc[:, 0].values
    #print(i)
    Vs_all, depth_all, tts_all, base_tts, std_tts, std_Vs, depth_inter = Travel_time(Vs, Depth, fig_plot=True, 
                                                                                     save_file=False, filename=i)
    results[i] = [std_tts, std_Vs, depth_inter]

# Create a DataFrame from the results dictionary
results_df = pd.DataFrame.from_dict(results, orient='index', columns=['std_tts', 'std_Vs','depth_inter'])

# Extract the maximum depth from the results
max_Depth = results_df['depth_inter'].apply(max).max()

## Plot the results for each index across depth of std_tts
for idx, i in enumerate(results_df.index):
    plt.plot(results_df.loc[i, 'std_tts'], results_df.loc[i, 'depth_inter'], label=i)

plt.title('Standard Deviation of Travel Time')
plt.vlines(0.05, 0, max_Depth, colors='red')
plt.text(0.05+0.002, max_Depth*0.95, 'Input: '+str(0.05), rotation=90, color='red', fontsize=10)
plt.ylabel('Depth (m)')
plt.ylim(0, max_Depth)
plt.xlim(0, 0.1)
plt.xlabel(r'$\sigma_{ln tts}$')
plt.legend(fontsize=9.5)

# Get the current Axes object and invert the y-axis
ax = plt.gca()
ax.invert_yaxis()
# Put horizontal ticks on the top
ax.xaxis.tick_top()
# Put horizontal title on the top
ax.xaxis.set_label_position('top')

# Save the figure
plt.savefig('Examples/Randomized_Results.png', dpi=300, bbox_inches='tight')
plt.show()

## Plot the results for each index across depth of std_Vs
for idx, i in enumerate(results_df.index):
    plt.plot(results_df.loc[i, 'std_Vs'], results_df.loc[i, 'depth_inter'], label=i)

plt.title('Standard Deviation of Vs')
plt.vlines(0.05, 0, max_Depth, colors='red')
plt.text(0.05+0.002, max_Depth*0.95, 'Input: '+str(0.05), rotation=90, color='red', fontsize=10)
plt.ylabel('Depth (m)')
plt.ylim(0, max_Depth)
plt.xlim(0, 0.5)
plt.xlabel(r'$\sigma_{ln Vs}$')
plt.legend(fontsize=9.5)

# Get the current Axes object and invert the y-axis
ax = plt.gca()
ax.invert_yaxis()
# Put horizontal ticks on the top
ax.xaxis.tick_top()
# Put horizontal title on the top
ax.xaxis.set_label_position('top')

# Save the figure
plt.savefig('Examples/Randomized_Results_Vs.png', dpi=300, bbox_inches='tight')
plt.show()



