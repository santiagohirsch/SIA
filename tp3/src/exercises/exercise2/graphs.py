import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_testing_error_vs_k_linear_ordered():
    plot_testing_error_vs_k('linear_perceptron_test_errors_ordered', 'IDENTITY', 'Ordered')

def plot_testing_error_vs_k_linear_shuffled():
    plot_testing_error_vs_k('linear_perceptron_test_errors_shuffled', 'IDENTITY', 'Shuffled')

def plot_testing_error_vs_k_non_linear_sigmoid_shuffled():
    plot_testing_error_vs_k('non_linear_perceptron_test_errors_sigmoid_shuffled', 'SIGMOID', 'Shuffled')

def plot_testing_error_vs_k_non_linear_sigmoid_ordered():
    plot_testing_error_vs_k('non_linear_perceptron_test_errors_sigmoid_ordered', 'SIGMOID', 'Ordered')

def plot_testing_error_vs_k_non_linear_tanh_shuffled():
    plot_testing_error_vs_k('non_linear_perceptron_test_errors_tanh_shuffled', 'TANH', 'Shuffled')

def plot_testing_error_vs_k_non_linear_tanh_ordered():
    plot_testing_error_vs_k('non_linear_perceptron_test_errors_tanh_ordered', 'TANH', 'Ordered')

def plot_testing_error_vs_k(file_prefix, activation, data_type):
    for i in range(2, 6):
        # Load the CSV file
        df = pd.read_csv(f'{file_prefix}_k{i}.csv')

        # Extract the columns k and test_errors
        k_values = df['k']
        test_errors = df['test_errors']

        # Create the bar plot
        plt.figure(figsize=(8, 6))
        plt.bar(range(len(k_values)), test_errors, color='blue')

        # Set the k values on the x-axis
        plt.xticks(range(len(k_values)), k_values)
        # Add labels and title
        plt.xlabel('K')
        plt.ylabel('Test Errors')
        plt.title(f'{activation} - Test Error vs. K - {data_type} Data - K={i}')
        ax = plt.gca()
        ax.set_axisbelow(True)
        plt.grid(True, axis='y')
        plt.show()

def plot_testing_error_vs_epochs_non_linear_tanh_shuffled():
    
    for m in range(2, 6):
        # Load the CSV file
        df = pd.read_csv(f'non_linear_perceptron_tanh_test_errors_vs_epochs_k{m}.csv')

        grouped = df.groupby('k')

        # Initialize the plot
        fig, ax = plt.subplots()

        # Set the width of the bars
        bar_width = 0.35

        # Get unique epochs across all groups
        unique_epochs = df['epochs'].unique()

        # Calculate the total width for each group of bars
        group_width = bar_width * len(grouped)

        # Calculate the space between groups
        space_between = 0.2

        # Calculate the offset for each group of bars
        offset = np.arange(len(unique_epochs)) * (group_width + space_between)

        # Iterate over each group (k value)
        for i, (k, group) in enumerate(grouped):
            # Extract epochs and test errors for the current group
            epochs = group['epochs']
            test_errors = group['test_errors']

            # Calculate x positions for bars
            x = offset + i * bar_width

            # Plot bars
            ax.bar(x, test_errors, bar_width, label=f'k = {k}')

        # Set x-axis ticks and labels
        ax.set_xticks(offset + group_width / 2)
        ax.set_xticklabels(unique_epochs)

        # Add labels and title
        ax.set_xlabel('Epochs')
        ax.set_ylabel('Test Errors')
        ax.set_title(f'Non Linear (TANH) - Test Error vs. Epochs - Shuffled Data - K={m}')
        ax.legend()
        ax.grid(axis='y')
        ax.set_axisbelow(True)
        ax.set_ylim(0, df['test_errors'].max()/4)
        # Show the plot
        plt.tight_layout()
        plt.show()

# plot_testing_error_vs_k_linear_ordered()
# plot_testing_error_vs_k_linear_shuffled()
# plot_testing_error_vs_k_non_linear_sigmoid_shuffled()
# plot_testing_error_vs_k_non_linear_sigmoid_ordered()
# plot_testing_error_vs_k_non_linear_tanh_shuffled()
# plot_testing_error_vs_k_non_linear_tanh_ordered()
plot_testing_error_vs_epochs_non_linear_tanh_shuffled()