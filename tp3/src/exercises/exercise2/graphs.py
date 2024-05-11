import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_training_error_vs_epoch_linear():

    # Load the CSV file
    df = pd.read_csv('linear_perceptron_results.csv')

    # Get unique values of k
    unique_k_values = df['k'].unique()

    # Plot each k value separately
    for k_value in range(5,6):
        # Filter the dataframe for the current k value
        df_k = df[df['k'] == k_value]
        
        # Plot training error vs. epoch for the current k value
        plt.plot(df_k['epoch'][:2000], df_k['training_error'][:2000], label=f'k = {k_value}')

    # Add labels and legend
    plt.xlabel('Epoch')
    plt.ylabel('Training Error')
    plt.title('Linear (IDENTITY) - Training Error vs. Epoch for Different k Values')
    plt.legend()

    # Show the plot
    plt.show()

def plot_testing_error_vs_epoch_linear():

    # Load the CSV file
    df = pd.read_csv('linear_perceptron_results.csv')

    # Get unique values of k
    unique_k_values = df['k'].unique()

    # Plot each k value separately
    for k_value in range(5,6):
        # Filter the dataframe for the current k value
        df_k = df[df['k'] == k_value]
        
        # Plot testing error vs. epoch for the current k value
        plt.plot(df_k['epoch'][:2000], df_k['test_error'][:2000], label=f'k = {k_value}')

    # Add labels and legend
    plt.xlabel('Epoch')
    plt.ylabel('Testing Error')
    plt.title('Linear (IDENTITY) - Testing Error vs. Epoch for Different k Values')
    plt.legend()

    # plt.ylim(0, 4000)

    # Show the plot
    plt.show()

def plot_training_error_vs_epoch_non_linear_sigmoid():
    # Load the CSV file
    df = pd.read_csv('non_linear_perceptron_results_sigmoid.csv')

    # Get unique values of beta
    unique_beta_values = df['beta'].unique()

    # Plot one graph per beta
    for beta_value in unique_beta_values:
        # Filter the dataframe for the current beta value
        df_beta = df[df['beta'] == beta_value]
        
        # Get unique values of k for the current beta value
        unique_k_values = df_beta['k'].unique()
        
        # Plot each k value separately
        for k_value in range(5,6):
            # Filter the dataframe for the current k value
            df_k = df_beta[df_beta['k'] == k_value]
            
            # Plot training error vs. epoch for the current k value and beta value
            plt.plot(df_k['epoch'][:1750], df_k['training_error'][:1750], label=f'k = {k_value}')

        # Add labels and legend
        plt.xlabel('Epoch')
        plt.ylabel('Training Error')
        plt.title(f'Non Linear (SIGMOID) - Training Error vs. Epoch for Different k Values, beta = {beta_value}')
        plt.legend()
        
        # Show the plot for the current beta value
        plt.show()

def plot_testing_error_vs_k_non_linear_sigmoid():
   # Load the CSV file
    df = pd.read_csv('non_linear_perceptron_test_errors_sigmoid.csv')

    # Get unique values of beta
    unique_beta_values = df['beta'].unique()

    # Initialize figure and axis
    fig, ax = plt.subplots()

    # Set width of bars
    bar_width = 0.35

    # Iterate over unique beta values
    for i, beta_value in enumerate(unique_beta_values):
        # Filter the dataframe for the current beta value
        df_beta = df[df['beta'] == beta_value]
        
        # Get k values and corresponding test errors for the current beta value
        k_values = df_beta['k']
        test_errors = df_beta['test_errors']
        
        # Set x positions for bars
        x = np.arange(len(k_values)) + i * bar_width
        
        # Plot bars
        ax.bar(x, test_errors, bar_width, label=f'beta = {beta_value}')

    # Set labels and title
    ax.set_xlabel('k')
    ax.set_ylabel('Test Error')
    ax.set_title('Test Error vs. k for Different Beta Values')
    ax.set_xticks(np.arange(len(k_values)) + bar_width / 2)
    ax.set_xticklabels(k_values)
    ax.legend()

    # Show the plot
    plt.show()

def plot_training_error_vs_epoch_non_linear_tanh():
    # Load the CSV file
    df = pd.read_csv('non_linear_perceptron_results_tanh.csv')

    # Get unique values of beta
    unique_beta_values = df['beta'].unique()

    # Plot one graph per beta
    for beta_value in unique_beta_values:
        # Filter the dataframe for the current beta value
        df_beta = df[df['beta'] == beta_value]
        
        # Get unique values of k for the current beta value
        unique_k_values = df_beta['k'].unique()
        
        # Plot each k value separately
        for k_value in range(5,6):
            # Filter the dataframe for the current k value
            df_k = df_beta[df_beta['k'] == k_value]
            
            # Plot training error vs. epoch for the current k value and beta value
            plt.plot(df_k['epoch'][:500], df_k['training_error'][:500], label=f'k = {k_value}')

        # Add labels and legend
        plt.xlabel('Epoch')
        plt.ylabel('Training Error')
        plt.title(f'Non Linear (TANH) - Training Error vs. Epoch for Different k Values, beta = {beta_value}')
        plt.legend()
        
        # Show the plot for the current beta value
        plt.show()

def plot_testing_error_vs_epoch_non_linear_tanh():
    # Load the CSV file
    df = pd.read_csv('non_linear_perceptron_results_tanh.csv')

    # Get unique values of beta
    unique_beta_values = df['beta'].unique()

    # Plot one graph per beta
    for beta_value in unique_beta_values:
        # Filter the dataframe for the current beta value
        df_beta = df[df['beta'] == beta_value]
        
        # Get unique values of k for the current beta value
        unique_k_values = df_beta['k'].unique()
        
        # Plot each k value separately
        for k_value in range(5,6):
            # Filter the dataframe for the current k value
            df_k = df_beta[df_beta['k'] == k_value]
            
            # Plot testing error vs. epoch for the current k value and beta value
            plt.plot(df_k['epoch'][:500], df_k['test_error'][:500], label=f'k = {k_value}')

        # Add labels and legend
        plt.xlabel('Epoch')
        plt.ylabel('Testing Error')
        plt.title(f'Non Linear (TANH) - Testing Error vs. Epoch for Different k Values, beta = {beta_value}')
        plt.legend()
        
        # Show the plot for the current beta value
        plt.show()

# plot_training_error_vs_epoch_linear()
# plot_testing_error_vs_epoch_linear()
plot_training_error_vs_epoch_non_linear_sigmoid()
plot_testing_error_vs_k_non_linear_sigmoid()
# plot_training_error_vs_epoch_non_linear_tanh()
# plot_testing_error_vs_epoch_non_linear_tanh()