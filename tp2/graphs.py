import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.utils.class_utils import CHARACTER_TYPES

def create_graph(character):
    df = pd.read_csv('output/crossing_method.csv')
    crossing_methods = df['Crossing Method'].unique()
    iterations = df['Iteration'].unique()
    fitness = []
    mean_fitness = []
    std_dev_fitness = []

    for crossing_method in crossing_methods:
        for iteration in iterations:
            data = df[(df['Character'] == character) & (df['Crossing Method'] == crossing_method) & (df['Iteration'] == iteration)]
            if not data.empty:
                max_avg_fitness = data['Average Fitness'].max()
                fitness.append(max_avg_fitness)
        # Calculate mean and standard deviation of fitness
        mean_fitness.append(sum(fitness) / len(fitness))
        std_dev_fitness.append((sum((x - (sum(fitness) / len(fitness))) ** 2 for x in fitness) / len(fitness)) ** 0.5)

        # Plot the average fitness with standard deviation
        plt.errorbar(range(len(mean_fitness)), mean_fitness, yerr=std_dev_fitness, fmt='-o', label=f'{character} - {crossing_method}')

    # Set labels and title
    plt.xlabel('Iteration')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness per Iteration for each Character and Crossing Method')
    plt.legend()

    # Show the plot
    plt.show()

for character in CHARACTER_TYPES.keys():    
    create_graph(character)