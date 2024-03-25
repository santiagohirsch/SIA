import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo csv
df = pd.read_csv('results3.csv')

# Filter the dataframe to only include the specified algorithms
df = df[df['Algorithm'].isin(['astar', 'localgreedy', 'globalgreedy'])]

# Agrupar por heurística y algoritmo y calcular la duración media
grouped = df.groupby(['Algorithm', 'Heuristic'])['Nodes Expanded'].mean()

# Calculate standard deviation
std_dev = df.groupby(['Algorithm', 'Heuristic'])['Nodes Expanded'].std()


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
# Create a bar plot with error bars
ax = grouped.plot(kind='bar', yerr=std_dev, capsize=4)

# Set the title and labels
plt.title('Nodes Expanded per Algorithm for Map 3')
plt.xlabel('Algorithm')
plt.ylabel('Nodes Expanded')

plt.xticks(rotation=0)


# Add average values on top of each bar
for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy() 
    ax.annotate(f'{height}', (x + width/2, y + height*1.02), ha='center')

# Show the plot
plt.show()















