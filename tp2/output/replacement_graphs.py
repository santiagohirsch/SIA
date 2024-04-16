import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_avg_generation_count(data, combo, error_bar=True):
    plt.figure(figsize=(15, 5))
    filtered_data = data[data[['Replacement', 'First Selection Method', 'Second Selection Method']].apply(tuple, axis=1).isin([combo])]
    for character, char_data in filtered_data.groupby('Character'):
        generation_mean = char_data['Generation'].mean()
        plt.bar(character, generation_mean, label=character)
        plt.text(character, generation_mean, round(generation_mean, 2), ha='center', va='bottom')
        if error_bar:
            generation_std = char_data['Generation'].std()
            n = char_data['Generation'].count()
            if n > 1:
                generation_std /= np.sqrt(n)  # Normalize standard deviation
            plt.errorbar(character, generation_mean, yerr=generation_std, fmt='none', ecolor='black', capsize=5)
    plt.title(f'Average Generation Count for Combo {combo}')
    plt.xlabel('Character')
    plt.ylabel('Average Generation Count')
    plt.legend(loc='lower left')
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def plot_fitness_metrics(data, combo, error_bar=True):
    plt.figure(figsize=(15, 5))
    filtered_data = data[data[['Replacement', 'First Selection Method', 'Second Selection Method']].apply(tuple, axis=1).isin([combo])]
    characters = filtered_data['Character'].unique()
    bar_width = 0.35
    for i, character in enumerate(characters):
        char_data = filtered_data[filtered_data['Character'] == character]
        best_fitness_mean = char_data['Best Fitness'].mean()
        average_fitness_mean = char_data['Average Fitness'].mean()
        plt.bar(i - bar_width/2, best_fitness_mean, width=bar_width, label='Best Fitness', color='b')
        plt.bar(i + bar_width/2, average_fitness_mean, width=bar_width, label='Average Fitness', color='r')
        plt.text(i - bar_width/2, best_fitness_mean, round(best_fitness_mean, 2), ha='center', va='bottom')
        plt.text(i + bar_width/2, average_fitness_mean, round(average_fitness_mean, 2), ha='center', va='bottom')
        if error_bar:
            average_fitness_std = char_data['Average Fitness'].std()
            plt.errorbar(i + bar_width/2, average_fitness_mean, yerr=average_fitness_std, fmt='none', ecolor='black', capsize=5)
    plt.title(f'Best Fitness vs Average Fitness for Combo {combo}')
    plt.xlabel('Character')
    plt.ylabel('Fitness')
    plt.xticks(range(len(characters)), characters)
    #show legend only once
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc='lower left')
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def plot_coefficient_comparison(aggregated_data, top_combos):
    plt.figure(figsize=(10, 6))
    combo_labels = [f'{combo}' for combo in top_combos.index]
    coefficients = top_combos['Coefficient'].values
    std_errors = []

    for combo in top_combos.index:
        filtered_data = aggregated_data.xs(combo, level=['Replacement', 'First Selection Method', 'Second Selection Method'])
        std_error = filtered_data['Coefficient'].std()
        n = len(filtered_data)  # Number of samples
        normalized_std_error = std_error / np.sqrt(n)  # Normalize the standard error
        std_errors.append(normalized_std_error)

    plt.bar(combo_labels, coefficients, yerr=std_errors, capsize=5)
    for i, coef in enumerate(coefficients):
        plt.text(i, coef, round(coef, 2), ha='center', va='bottom')

    plt.title('Coefficient Comparison for Top 3 Combos')
    plt.xlabel('Combo')
    plt.ylabel('Coefficient')
    plt.yticks(np.arange(0, 41, 5))
    # plt.xticks(rotation=45)
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()


# Read the CSV file into a pandas DataFrame
df = pd.read_csv("output/replacement_method.csv")

# Group the data by "Character", "Replacement", "First Selection Method", and "Second Selection Method"
grouped = df.groupby(['Character', 'Replacement', 'First Selection Method', 'Second Selection Method'])

# Calculate the metrics for each combo
aggregated_data = grouped.agg({
    'Generation': 'mean',
    'Best Fitness': 'max',
    'Average Fitness': 'mean'
})

# Calculate the coefficient for each combo
coefficients = []
for (_, _, _, _), data in grouped:
    avg_generation_count = data['Generation'].mean()
    best_average_fitness = data['Average Fitness'].mean()
    if avg_generation_count != 0:
        coefficient = 10 / avg_generation_count + best_average_fitness
    else:
        coefficient = best_average_fitness  # Assigning infinity if avg_generation_count is zero
    coefficients.append(coefficient)

# Add the coefficient values to the aggregated data
aggregated_data['Coefficient'] = coefficients

# Find the top 3 combinations based on average coefficient
top_3_combinations = aggregated_data.groupby(level=[1, 2, 3]).mean().sort_values('Coefficient', ascending=False).head(3)

# Plot the desired generation graphs for each top combo
# for combo in top_3_combinations.index:
    # plot_avg_generation_count(df, combo, error_bar=True)
    # plot_fitness_metrics(df, combo, error_bar=True)

# Plot the coefficient comparison for the top 3 combinations
plot_coefficient_comparison(aggregated_data, top_3_combinations)
