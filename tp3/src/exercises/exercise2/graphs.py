import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_training_error_vs_epoch_linear():

    # Load the CSV file
    df = pd.read_csv('linear_perceptron_results.csv')

    # Get unique values of k
    unique_k_values = df['k'].unique()

    # Plot each k value separately
    for k_value in unique_k_values:
        # Filter the dataframe for the current k value
        df_k = df[df['k'] == k_value]
        
        # Plot training error vs. epoch for the current k value
        plt.plot(df_k['epoch'][:2000], df_k['training_error'][:2000], label=f'k = {k_value}')

    # Add labels and legend
    plt.xlabel('Epoch')
    plt.ylabel('Training Error')
    plt.title('Linear (IDENTITY) - Training Error vs. Epoch for Different k Values')
    plt.legend()
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')

    # Show the plot
    plt.show()

def plot_testing_error_vs_k_linear():

    # Load the CSV file
    df = pd.read_csv('linear_perceptron_test_errors.csv')

    # Extraer las columnas k y test_errors
    k_values = df['k']
    test_errors = df['test_errors']

    # Crear el gráfico de barras
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(k_values)), test_errors, color='blue')

    # Establecer los valores de k en el eje x
    plt.xticks(range(len(k_values)), k_values)
    # Añadir etiquetas y título
    plt.xlabel('k')
    plt.ylabel('Test Errors')
    plt.title('Linear (IDENTITY) - Test Error vs. k')
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')
    plt.show()

def plot_training_error_vs_epoch_non_linear_sigmoid():
    # Load the CSV file
    df = pd.read_csv('non_linear_perceptron_results_sigmoid.csv')

    # Get unique values of k
    unique_k_values = df['k'].unique()

    # Plot one graph per k value
    for k_value in unique_k_values:
        # Filter the dataframe for the current k value
        df_k = df[df['k'] == k_value]
        
        # Plot training error vs. epoch for the current k value
        plt.plot(df_k['epoch'][:1750], df_k['training_error'][:1750], label=f'k = {k_value}')

    # Add labels and legend
    plt.xlabel('Epoch')
    plt.ylabel('Training Error')
    plt.title('Non Linear (SIGMOID) - Training Error vs. Epoch for Different k Values')
    plt.legend()
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')
        
    # Show the plot
    plt.show()

def plot_testing_error_vs_k_non_linear_sigmoid():
   # Load the CSV file
    df = pd.read_csv('non_linear_perceptron_test_errors_sigmoid.csv')

    # Extraer las columnas k y test_errors
    k_values = df['k']
    test_errors = df['test_errors']

    # Crear el gráfico de barras
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(k_values)), test_errors, color='blue')

    # Establecer los valores de k en el eje x
    plt.xticks(range(len(k_values)), k_values)
    # Añadir etiquetas y título
    plt.xlabel('k')
    plt.ylabel('Test Errors')
    plt.title('Non Linear (SIGMOID) - Test Error vs. k')
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')
    plt.show()


def plot_training_error_vs_epoch_non_linear_tanh():
    # Load the CSV file
    df = pd.read_csv('non_linear_perceptron_results_tanh.csv')

    # Get unique values of k
    unique_k_values = df['k'].unique()

    # Plot one graph per k value
    for k_value in unique_k_values:
        # Filter the dataframe for the current k value
        df_k = df[df['k'] == k_value]
        
        # Plot training error vs. epoch for the current k value
        plt.plot(df_k['epoch'][:500], df_k['training_error'][:500], label=f'k = {k_value}')

    # Add labels and legend
    plt.xlabel('Epoch')
    plt.ylabel('Training Error')
    plt.title('Non Linear (TANH) - Training Error vs. Epoch for Different k Values')
    plt.legend()
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')
        
    # Show the plot
    plt.show()

def plot_testing_error_vs_k_non_linear_tanh():
   # Load the CSV file
    df = pd.read_csv('non_linear_perceptron_test_errors_tanh.csv')

    # Extraer las columnas k y test_errors
    k_values = df['k']
    test_errors = df['test_errors']

    # Crear el gráfico de barras
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(k_values)), test_errors, color='blue')

    # Establecer los valores de k en el eje x
    plt.xticks(range(len(k_values)), k_values)
    # Añadir etiquetas y título
    plt.xlabel('k')
    plt.ylabel('Test Errors')
    plt.title('Non Linear (TANH) - Test Error vs. k')
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')
    plt.show()



plot_training_error_vs_epoch_linear()
plot_testing_error_vs_k_linear()
plot_training_error_vs_epoch_non_linear_sigmoid()
plot_testing_error_vs_k_non_linear_sigmoid()
plot_training_error_vs_epoch_non_linear_tanh()
plot_testing_error_vs_k_non_linear_tanh()