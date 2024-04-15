import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_metric_vs_mutation_rate(df):
    # Group the data by Character, Mutation Method, and Mutation Rate
    grouped = df.groupby(['Character', 'Mutation Method', 'Mutation Rate'])


    aggregated_data = grouped.agg({
        'Best Fitness': 'max',
        'Average Fitness': 'mean',
        'Generation': 'mean'
    }).reset_index()

    # Step 3: Plot the data for each metric (Average Generation Count, Best Fitness, Average Fitness) divided by character
    metrics = ['Generation', 'Best Fitness', 'Average Fitness']
    ylabels = ['Average Generation Count', 'Best Fitness', 'Average Fitness']
    for metric in metrics:
        for character, char_data in aggregated_data.groupby('Character'):
            for method, method_data in char_data.groupby('Mutation Method'):
                plt.figure()
                plt.plot(method_data['Mutation Rate'], method_data[metric], 'o-', label=metric)
                plt.title(f'{character} - Mutation Method: {method}')
                plt.xlabel('Mutation Rate')
                plt.ylabel(ylabels[metrics.index(metric)])
                plt.legend()
                ax = plt.gca()
                ax.set_axisbelow(True)
                plt.xticks(np.arange(0, 1.05, 0.05))  # Set x-axis ticks with intervals of 0.05 jumps
                plt.grid(True)
                plt.show()

def plot_average_coefficient(df):
    # Group the data by Mutation Method and Mutation Rate
    grouped = df.groupby(['Mutation Method', 'Mutation Rate'])

    # Aggregate the data to calculate the average coefficient per mutation method per mutation rate
    aggregated_data = grouped.agg({
        'Best Fitness': 'max',
        'Average Fitness': 'mean',
        'Generation': 'mean'
    }).reset_index()

    # Calculate the coefficients
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

    # Add the coefficient values to the aggregated data
    aggregated_data['Coefficient'] = coefficients

    # Plot the average coefficient per mutation method per mutation rate
    plt.figure()
    for method, data in aggregated_data.groupby('Mutation Method'):
        plt.plot(data['Mutation Rate'], data['Coefficient'], 'o-', label=method)
    plt.title('Average Coefficient per Mutation Method and Rate')
    plt.xlabel('Mutation Rate')
    plt.ylabel('Average Coefficient')
    plt.legend()
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.xticks(np.arange(0, 1.05, 0.05))  # Set x-axis ticks with intervals of 0.05 jumps
    plt.grid(True)
    plt.show()

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("/Users/santiago/Desktop/ITBA/1C2024/SIA/SIA/tp2/output/mutation_method.csv")

# Call the functions to plot the graphs
plot_metric_vs_mutation_rate(df)
plot_average_coefficient(df)