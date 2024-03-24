import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo csv
df = pd.read_csv('results.csv')

# Filter the dataframe to only include the specified algorithms
df = df[df['Algorithm'].isin(['astar', 'localgreedy', 'globalgreedy'])]

# Agrupar por heurística y algoritmo y calcular la duración media
grouped = df.groupby(['Heuristic', 'Algorithm'])['Duration'].mean()

# Calculate standard deviation
std_dev = df.groupby(['Heuristic', 'Algorithm'])['Duration'].std()


# Unstack the grouped data to create a multi-bar plot
grouped = grouped.unstack()

# Calculate standard deviation for each group
std_dev = std_dev.unstack()


# Create a bar plot with error bars
grouped.plot(kind='bar', yerr=std_dev, capsize=4)

# Set the title and labels
plt.title('Average Duration with Error Bars')
plt.xlabel('Heuristic and Algorithm')
plt.ylabel('Average Duration')

# Show the plot
plt.show()