import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_avg_generation_count(data, first_sel_method, error_bar=True):
    for first_sel_method, first_sel_data in data.groupby(level=0):
        for character, char_data in first_sel_data.groupby(level=1):
            plt.figure()
            ax = char_data['Generation'].plot(kind='bar', yerr=char_data['Generation'].std() if error_bar else None, capsize=5)
            ax.set_title(f'Average Generation Count for {first_sel_method} - Character {character}')
            ax.set_xlabel('Second Selection Method')
            ax.set_ylabel('Average Generation Count')
            ax.set_xticklabels(char_data.index.get_level_values('Second Selection Method'), rotation=45)
            # Add text annotations
            for i, generation in enumerate(char_data['Generation']):
                ax.text(i, generation, round(generation, 2), ha='center', va='bottom')
            plt.tight_layout()
            ax = plt.gca()
            ax.set_axisbelow(True)
            plt.grid(axis='y')
            plt.show()

def plot_fitness_metrics(data, first_sel_method, error_bar=True):
    for first_sel_method, first_sel_data in data.groupby(level=0):
        for character, char_data in first_sel_data.groupby(level=1):
            plt.figure()
            index = np.arange(len(char_data))
            bar_width = 0.35

            # Plot Best Fitness bars
            plt.bar(index, char_data['Best Fitness'], bar_width, label='Best Fitness', color='b')

            # Plot Average Fitness bars
            plt.bar(index + bar_width, char_data['Average Fitness'], bar_width, label='Average Fitness', color='r')

            # Add error bars only for Average Fitness
            if error_bar:
                plt.errorbar(index + bar_width, char_data['Average Fitness'], 
                             yerr=char_data['Average Fitness'].std(), fmt='none', ecolor='black', capsize=5)
            
            # Add text annotations
            for i, (best, avg) in enumerate(zip(char_data['Best Fitness'], char_data['Average Fitness'])):
                plt.text(i, best, round(best, 2), ha='center', va='bottom')
                plt.text(i + bar_width, avg, round(avg, 2), ha='center', va='bottom')

            plt.title(f'Best and Average Fitness for {first_sel_method} - Character {character}')
            plt.xlabel('Second Selection Method')
            plt.ylabel('Fitness')
            plt.xticks(index + bar_width / 2, char_data.index.get_level_values('Second Selection Method'), rotation=45)
            plt.legend()
            plt.tight_layout()
            ax = plt.gca()
            ax.set_axisbelow(True)
            plt.grid(axis='y')
            plt.show()

def plot_avg_coefficient(data):
    plt.figure()
    for first_sel_method, first_sel_data in data.groupby(level=0):
        coefficients = first_sel_data.groupby('Second Selection Method')['Coefficient'].mean()
        errors = first_sel_data.groupby('Second Selection Method')['Coefficient'].std()
        plt.bar(coefficients.index, coefficients.values, label=first_sel_method)
        for i, (coef, err) in enumerate(zip(coefficients.values, errors.values)):
            plt.errorbar(i, coef, yerr=err, fmt='none', ecolor='black', capsize=5)
            plt.text(i, coef, round(coef, 2), ha='center', va='bottom')
    plt.title(f'Average Coefficient for {first_sel_method}')
    plt.xlabel('Second Selection Method')
    plt.ylabel('Average Coefficient')
    plt.xticks(range(len(coefficients)), coefficients.index, rotation=45)
    plt.tight_layout()
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(axis='y')
    plt.show()




# Step 1: Read the CSV file into a pandas DataFrame
df = pd.read_csv("output/selection_method.csv")

# Step 2: Group the data by "First Selection Method", "Character", and "Second Selection Method"
grouped = df.groupby(['First Selection Method', 'Character', 'Second Selection Method'])

# Step 3: Calculate the metrics for each combo
aggregated_data = grouped.agg({
    'Generation': 'mean',
    'Best Fitness': 'max',
    'Average Fitness': 'mean'
})

# Calculate the coefficient for each combo
coefficients = []
for (_, _, first_sel_method), data in grouped:
    avg_generation_count = data['Generation'].mean()
    best_average_fitness = data['Average Fitness'].mean()
    if avg_generation_count != 0:
        coefficient = 10 / avg_generation_count + best_average_fitness
    else:
        coefficient = best_average_fitness  # Assigning infinity if avg_generation_count is zero
    coefficients.append(coefficient)

# Add the coefficient values to the aggregated data
aggregated_data['Coefficient'] = coefficients

# Step 4: Plot the desired graphs for each "First Selection Method"
for first_sel_method, data in aggregated_data.groupby(level=0):
    plot_avg_generation_count(data, first_sel_method, error_bar=True)
    plot_fitness_metrics(data, first_sel_method, error_bar=True)
    plot_avg_coefficient(data)
