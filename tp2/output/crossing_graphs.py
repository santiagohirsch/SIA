import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a pandas DataFrame
df = pd.read_csv("/Users/santiago/Desktop/ITBA/1C2024/SIA/SIA/tp2/output/crossing_method.csv")

# Step 2: Group the data by Character and Crossing Method
grouped = df.groupby(['Character', 'Crossing Method'])

# Step 3: Calculate the average generation count per crossing method
average_generation_count = grouped['Generation'].mean().reset_index()

# Step 4: Plot the data for each character
for character, data in average_generation_count.groupby('Character'):
    plt.figure()
    bars = plt.bar(data['Crossing Method'], data['Generation'])
    plt.title(f'Average Generation Count per Crossing Method - Character {character}')
    plt.xlabel('Crossing Method')
    plt.ylabel('Average Generation Count')
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')
    
    # Add error bars
    plt.errorbar(data['Crossing Method'], data['Generation'], yerr=data['Generation'].std(), fmt='none', ecolor='black', capsize=5)
    
    # Add text annotations
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), round(bar.get_height(), 2),
                 ha='center', va='bottom')
    
    plt.show()

# Step 5: Calculate the average and best fitness per crossing method
average_best_fitness = grouped['Best Fitness'].max().reset_index()
average_average_fitness = grouped['Average Fitness'].mean().reset_index()

# Step 6: Plot the data for each character
for character, data in average_best_fitness.groupby('Character'):
    plt.figure()
    bar_width = 0.35
    index = np.arange(len(data['Crossing Method']))
    
    bars1 = plt.bar(index, data['Best Fitness'], bar_width, label='Best Fitness', color='b')
    bars2 = plt.bar(index + bar_width, average_average_fitness[average_average_fitness['Character'] == character]['Average Fitness'],
            bar_width, label='Average Fitness', color='r')
    
    for bar1, bar2 in zip(bars1, bars2):
        plt.text(bar1.get_x() + bar1.get_width() / 2, bar1.get_height(), round(bar1.get_height(), 2),
                 ha='center', va='bottom')
        plt.text(bar2.get_x() + bar2.get_width() / 2, bar2.get_height(), round(bar2.get_height(), 2),
                 ha='center', va='bottom')
    
    # Add error bars only to the bars representing average fitness
    plt.errorbar(index + bar_width , average_average_fitness[average_average_fitness['Character'] == character]['Average Fitness'],
                 yerr=df.groupby(['Character', 'Crossing Method'])['Average Fitness'].std().loc[character].values, fmt='none', ecolor='black', capsize=5)
    
    plt.title(f'Average and Best Fitness per Crossing Method - Character {character}')
    plt.xlabel('Crossing Method')
    plt.ylabel('Fitness')
    plt.xticks(index + bar_width / 2, data['Crossing Method'])
    plt.legend(loc='lower right')
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')
    plt.show()

aggregated_data = grouped.agg({
    'Best Fitness': 'max',
    'Average Fitness': 'mean',
    'Generation': 'mean'
}).reset_index()

coefficients = []
for _, row in aggregated_data.iterrows():
    best_average_fitness = row['Average Fitness']
    average_generation_count = row['Generation']
    
    # Check if average_generation_count is not zero to avoid division by zero
    if average_generation_count != 0:
        coefficient = 10 / average_generation_count + best_average_fitness
    else:
        coefficient = best_average_fitness  # Assigning infinity if average_generation_count is zero
    
    coefficients.append(coefficient)

# Step 7: Add the coefficient values to the aggregated data
aggregated_data['Coefficient'] = coefficients

# Step 8: Group the aggregated data by Crossing Method and calculate the average coefficient per method
average_coefficient = aggregated_data.groupby('Crossing Method')['Coefficient'].mean().reset_index()
# Step 9: Plot the data
plt.figure()
bars = plt.bar(average_coefficient['Crossing Method'], average_coefficient['Coefficient'])
plt.title('Average Coefficient per Crossing Method')
plt.xlabel('Crossing Method')
plt.ylabel('Average Coefficient')
ax = plt.gca()
ax.set_axisbelow(True)
plt.grid(True, axis='y')

# Calculate the positions for error bars to be located in the middle of the bars representing average coefficient
positions = np.arange(len(average_coefficient['Crossing Method']))
plt.errorbar(positions, average_coefficient['Coefficient'],
             yerr=aggregated_data.groupby('Crossing Method')['Coefficient'].std().values, fmt='none', ecolor='black', capsize=5)

# Add text annotations
for bar, position in zip(bars, positions):
    plt.text(position, bar.get_height(), round(bar.get_height(), 2),
             ha='center', va='bottom')

plt.xticks(positions, average_coefficient['Crossing Method'])
plt.show()
