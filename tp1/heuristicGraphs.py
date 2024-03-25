import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo csv
df = pd.read_csv('results2.csv')

# Filter the dataframe to only include the specified algorithms
df = df[df['Algorithm'].isin(['astar', 'localgreedy', 'globalgreedy'])]

# Agrupar por heurística y algoritmo y calcular la duración media
grouped = df.groupby(['Algorithm', 'Heuristic'])['Duration'].mean()

# Calculate standard deviation
std_dev = df.groupby(['Algorithm', 'Heuristic'])['Duration'].std()


# Unstack the grouped data to create a multi-bar plot
grouped = grouped.unstack()

# Calculate standard deviation for each group
std_dev = std_dev.unstack()


grouped.rename(index={'localgreedy': 'Local Greedy'}, inplace=True)
std_dev.rename(index={'localgreedy': 'Local Greedy'}, inplace=True)

grouped.rename(index={'globalgreedy': 'Global Greedy'}, inplace=True)
std_dev.rename(index={'globalgreedy': 'Global Greedy'}, inplace=True)

grouped.rename(index={'astar': 'A*'}, inplace=True)
std_dev.rename(index={'astar': 'A*'}, inplace=True)



grouped.rename(columns={'manhattan': 'Manhattan'}, inplace=True)
std_dev.rename(columns={'manhattan': 'Manhattan'}, inplace=True)

grouped.rename(columns={'improvedman': 'Improved Manhattan'}, inplace=True)
std_dev.rename(columns={'improvedman': 'Improved Manhattan'}, inplace=True)


# Create a bar plot with error bars
grouped.plot(kind='bar', yerr=std_dev, capsize=4)

# Set the title and labels
plt.title('Duration per Algorithm for Map 2')
plt.xlabel('Algorithm')
plt.ylabel('Duration in Seconds')

plt.xticks(rotation=0)

# Show the plot
plt.show()