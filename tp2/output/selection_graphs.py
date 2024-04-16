import pandas as pd
import matplotlib.pyplot as plt

def plot_avg_generation_count(data, first_sel_method, error_bar=True):
    plt.figure()
    ax = data['Generation'].plot(kind='bar', yerr=data['Generation'].std() if error_bar else None, capsize=5)
    ax.set_title(f'Average Generation Count for {first_sel_method}')
    ax.set_xlabel('Second Selection Method')
    ax.set_ylabel('Average Generation Count')
    ax.set_xticklabels(data.index.get_level_values('Second Selection Method'), rotation=45)
    plt.tight_layout()
    plt.show()

def plot_fitness_metrics(data, first_sel_method, error_bar=True):
    plt.figure()
    error_values = data[['Best Fitness', 'Average Fitness']].std() if error_bar else None
    ax = data[['Best Fitness', 'Average Fitness']].plot(kind='bar', yerr=error_values, capsize=5)
    ax.set_title(f'Best and Average Fitness for {first_sel_method}')
    ax.set_xlabel('Second Selection Method')
    ax.set_ylabel('Fitness')
    ax.set_xticklabels(data.index.get_level_values('Second Selection Method'), rotation=45)
    plt.tight_layout()
    plt.show()

def plot_avg_coefficient(data, first_sel_method):
    plt.figure()
    ax = data['Coefficient'].plot(kind='bar', color='blue', yerr=data['Coefficient'].std(), capsize=5)
    ax.set_title(f'Average Coefficient for {first_sel_method}')
    ax.set_xlabel('Second Selection Method')
    ax.set_ylabel('Average Coefficient')
    ax.set_xticklabels(data.index.get_level_values('Second Selection Method'), rotation=45)
    plt.tight_layout()
    plt.show()


# Step 1: Read the CSV file into a pandas DataFrame
df = pd.read_csv("output/selection_method.csv")

# Step 2: Group the data by "First Selection Method" and "Second Selection Method"
grouped = df.groupby(['First Selection Method', 'Second Selection Method'])

# Step 3: Calculate the metrics for each combo
aggregated_data = grouped.agg({
    'Generation': 'mean',
    'Best Fitness': 'max',
    'Average Fitness': 'mean'
})

# Calculate the coefficient for each combo
coefficients = []
for (_, first_sel_method), data in grouped:
    avg_generation_count = data['Generation'].mean()
    best_average_fitness = data['Average Fitness'].mean()
    if avg_generation_count != 0:
        coefficient = 10 / avg_generation_count + best_average_fitness
    else:
        coefficient = best_average_fitness  # Assigning infinity if avg_generation_count is zero
    coefficients.append(coefficient)

aggregated_data['Coefficient'] = coefficients

# Step 4: Plot the desired graphs for each "First Selection Method"
for first_sel_method, data in aggregated_data.groupby(level=0):
    plot_avg_generation_count(data, first_sel_method, error_bar=True)
    plot_fitness_metrics(data, first_sel_method, error_bar=True)
    plot_avg_coefficient(data, first_sel_method)
