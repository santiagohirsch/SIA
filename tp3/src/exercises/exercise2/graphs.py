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

def plot_training_error_vs_epoch_linear():
    # Load the CSV file
    df = pd.read_csv('linear_perceptron_training_errors.csv')

    # Extract the columns epoch and error
    epochs = df['epoch']
    errors = df['error']

    # Create the line plot with dots
    plt.figure(figsize=(8, 6))
    plt.plot(epochs, errors, color='blue', marker='o', linestyle='-', markevery=100)  # Add markevery parameter

    # Add labels and title
    plt.xlabel('Epochs')
    plt.ylabel('Training Errors')
    plt.title('Linear (IDENTITY) - Training Error vs. Epochs - Ordered Data')
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')

    # Add more y-ticks
    plt.yticks(np.arange(0, max(errors)+500, 1000))

    plt.show()

def plot_training_error_vs_epoch_non_linear_sigmoid():
    # Load the CSV file
    df = pd.read_csv('non_linear_perceptron_sigmoid_training_errors.csv')

    # Extract the columns epoch and error
    epochs = df['epoch']
    errors = df['error']

    # Create the line plot with dots
    plt.figure(figsize=(8, 6))
    plt.plot(epochs, errors, color='blue', marker='o', linestyle='-', markevery=100)

    # Add labels and title
    plt.xlabel('Epochs')
    plt.ylabel('Training Errors')
    plt.title('Non-Linear (SIGMOID) - Training Error vs. Epochs - Ordered Data')
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')

    # Add more y-ticks
    plt.yticks(np.arange(0, max(errors)+0.1, 0.05))

    plt.show()

def plot_training_error_vs_epoch_non_linear_tanh():
    # Load the CSV file
    df = pd.read_csv('non_linear_perceptron_tanh_training_errors.csv')

    # Extract the columns epoch and error
    epochs = df['epoch']
    errors = df['error']

    # Create the line plot with dots
    plt.figure(figsize=(8, 6))
    plt.plot(epochs, errors, color='blue', marker='o', linestyle='-', markevery=100)

    # Add labels and title
    plt.xlabel('Epochs')
    plt.ylabel('Training Errors')
    plt.title('Non-Linear (TANH) - Training Error vs. Epochs - Ordered Data')
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')
    # Add more y-ticks
    plt.yticks(np.arange(0, max(errors)+0.5, 0.5))

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

def plot_testing_error_vs_epochs_non_linear_sigmoid_shuffled():
    for m in range(2, 6):
        # Load the CSV file
        df = pd.read_csv(f'non_linear_perceptron_sigmoid_test_errors_vs_epochs_k{m}.csv')

        grouped = df.groupby('epochs')

        # Initialize the plot
        fig, ax = plt.subplots()

        # Set the width of the bars
        bar_width = 0.35

        # Get unique epochs across all groups
        unique_epochs = df['epochs'].unique()

        # Calculate the total width for each group of bars
        group_width = bar_width * m

        # Calculate the space between groups
        space_between = bar_width

        # Calculate the offset for each group of bars
        offset = np.arange(len(unique_epochs)) * (group_width + space_between)

        colors = ['blue', 'red', 'green', 'orange', 'purple']
        labels = ['K = 1', 'K = 2', 'K = 3', 'K = 4', 'K = 5']
        # Iterate over each group (k value)
        for i, (k, group) in enumerate(grouped):
            # Extract epochs and test errors for the current group
            test_errors = group['test_errors']

            # Calculate x positions for bars
            x = []
            for j in range(len(test_errors)):
                # Calculate the distance of the bar from the center
                distance_from_center = j - (m - 1) / 2
                # Calculate the x position of the bar
                x_position = offset[i] + group_width / 2 + distance_from_center * (bar_width)
                x.append(x_position)

            # Plot bars
            ax.bar(x, test_errors, bar_width, color=colors[:m])

        # Set x-axis ticks and labels
        ax.set_xticks(offset + group_width / 2)
        ax.set_xticklabels(unique_epochs)
        handles = [plt.Rectangle((0,0),1,1, color=colors[i], ec="k") for i in range(len(colors[:m]))]
        ax.legend(handles, labels[:m])
        # Add labels and title
        ax.set_xlabel('Epochs')
        ax.set_ylabel('Test Errors')
        ax.set_title(f'Non Linear (SIGMOID) - Test Error vs. Epochs - Shuffled Data - K={m}')

        ax.grid(axis='y')
        ax.set_axisbelow(True)
        ax.set_ylim(0, df['test_errors'].max()/100)
        # Show the plot
        plt.tight_layout()
        plt.show()

def plot_testing_error_vs_beta_non_linear_tanh_shuffled():
    df = pd.read_csv("non_linear_perceptron_tanh_test_errors_vs_beta.csv")
    grouped = df.groupby('beta')

    # Initialize the plot
    fig, ax = plt.subplots()

    # Set the width of the bars
    bar_width = 0.35

    # Get unique epochs across all groups
    unique_betas = df['beta'].unique()

    # Calculate the total width for each group of bars
    group_width = bar_width * len(grouped)

    # Calculate the space between groups
    space_between = 0.2

    # Calculate the offset for each group of bars
    offset = np.arange(len(unique_betas)) * (group_width + space_between)

    # Iterate over each group (k value)
    for i, (k, group) in enumerate(grouped):
        # Extract epochs and test errors for the current group
        test_errors = group['test_errors']

        # Calculate x positions for bars
        x = offset + i * bar_width

        # Plot bars
        ax.bar(x, test_errors, bar_width, label=f'K = {k}')

    # Set x-axis ticks and labels
    ax.set_xticks(offset + group_width / 2)
    ax.set_xticklabels(unique_betas)

    # Add labels and title
    ax.set_xlabel('Beta')
    ax.set_ylabel('Test Errors')
    ax.set_title('Non Linear (TANH) - Test Error vs. Beta - Shuffled Data')
    ax.legend()
    ax.grid(axis='y')
    ax.set_axisbelow(True)
    ax.set_ylim(0, df['test_errors'].max()/4)
    # Show the plot
    plt.tight_layout()
    plt.show()

def plot_testing_error_vs_beta_non_linear_sigmoid_shuffled():
    df = pd.read_csv("non_linear_perceptron_sigmoid_test_errors_vs_beta.csv")
    grouped = df.groupby('beta')

    # Initialize the plot
    fig, ax = plt.subplots()

    # Set the width of the bars
    bar_width = 0.35

    # Get unique epochs across all groups
    unique_betas = df['beta'].unique()

    # Calculate the total width for each group of bars
    group_width = bar_width * len(grouped)

    # Calculate the space between groups
    space_between = 0.2

    # Calculate the offset for each group of bars
    offset = np.arange(len(unique_betas)) * (group_width + space_between)

    colors = ['blue', 'red', 'green', 'orange', 'purple']
    labels = ['K = 1', 'K = 2', 'K = 3', 'K = 4', 'K = 5']

    # Iterate over each group (k value)
    for i, (k, group) in enumerate(grouped):
        # Extract epochs and test errors for the current group
        test_errors = group['test_errors']

        # Calculate x positions for bars
        x = []
        for j in range(len(test_errors)):
            # Calculate the distance of the bar from the center
            distance_from_center = j - (5 - 1) / 2
            # Calculate the x position of the bar
            x_position = offset[i] + group_width / 2 + distance_from_center * (bar_width)
            x.append(x_position)

        # Plot bars
        ax.bar(x, test_errors, bar_width, color=colors)

    ax.set_xticks(offset + group_width / 2)
    ax.set_xticklabels(unique_betas)

    # Add labels and title
    ax.set_xlabel('Beta')
    ax.set_ylabel('Test Errors')
    ax.set_title('Non Linear (SIGMOID) - Test Error vs. Beta - Shuffled Data')
    # Set custom legend with labels
    handles = [plt.Rectangle((0,0),1,1, color=colors[i], ec="k") for i in range(len(colors))]
    ax.legend(handles, labels)

    ax.grid(axis='y')
    ax.set_axisbelow(True)
    ax.set_ylim(0, df['test_errors'].max()/4)
    # Show the plot
    plt.tight_layout()
    plt.show()

def plot_testing_error_vs_learning_non_linear_sigmoid_shuffled():
    df = pd.read_csv("non_linear_perceptron_sigmoid_test_errors_vs_learning.csv")
    grouped = df.groupby('learning')

    # Initialize the plot
    fig, ax = plt.subplots()

    # Set the width of the bars
    bar_width = 0.35

    # Get unique epochs across all groups
    unique_learnings = df['learning'].unique()

    # Calculate the total width for each group of bars
    group_width = bar_width * len(grouped)

    # Calculate the space between groups
    space_between = 0.2

    # Calculate the offset for each group of bars
    offset = np.arange(len(unique_learnings)) * (group_width + space_between)

    colors = ['blue', 'red', 'green', 'orange', 'purple']
    labels = ['K = 1', 'K = 2', 'K = 3', 'K = 4', 'K = 5']
    # Iterate over each group (k value)
    for i, (k, group) in enumerate(grouped):
        # Extract epochs and test errors for the current group
        test_errors = group['test_errors']
        print(test_errors.mean())
        # Calculate x positions for bars
        x = []
        for j in range(len(test_errors)):
            # Calculate the distance of the bar from the center
            distance_from_center = j - (5 - 1) / 2
            # Calculate the x position of the bar
            x_position = offset[i] + group_width / 2 + distance_from_center * (bar_width)
            x.append(x_position)
        # Plot bars
        ax.bar(x, test_errors, bar_width, color=colors)

    # Set x-axis ticks and labels
    ax.set_xticks(offset + group_width / 2)
    ax.set_xticklabels(unique_learnings)

    # Add labels and title
    ax.set_xlabel('Learning Rate')
    ax.set_ylabel('Test Errors')
    ax.set_title('Non Linear (SIGMOID) - Test Error vs. Learning Rate - Shuffled Data')
    # Set custom legend with labels
    handles = [plt.Rectangle((0,0),1,1, color=colors[i], ec="k") for i in range(len(colors))]
    ax.legend(handles, labels)
    ax.grid(axis='y')
    ax.set_axisbelow(True)
    ax.set_ylim(0, df['test_errors'].max()/50)
    # Show the plot
    plt.tight_layout()
    plt.show()

def plot_testing_error_vs_batch_non_linear_sigmoid_shuffled():
    df = pd.read_csv("non_linear_perceptron_sigmoid_test_errors_vs_batch.csv")
    grouped = df.groupby('batch')

    # Initialize the plot
    fig, ax = plt.subplots()

    # Set the width of the bars
    bar_width = 0.15

    # Get unique epochs across all groups
    unique_batches = df['batch'].unique()

    # Calculate the total width for each group of bars
    group_width = bar_width * len(grouped)

    # Calculate the space between groups
    space_between = 0.5

    # Calculate the offset for each group of bars
    offset = np.arange(len(unique_batches)) * (group_width + space_between)

    colors = ['blue', 'red', 'green', 'orange', 'purple']
    labels = ['K = 1', 'K = 2', 'K = 3', 'K = 4', 'K = 5']
    # Iterate over each group (k value)
    for i, (k, group) in enumerate(grouped):
        # Extract epochs and test errors for the current group
        test_errors = group['test_errors']
        # Calculate x positions for bars
        x = []
        for j in range(len(test_errors)):
            # Calculate the distance of the bar from the center
            distance_from_center = j - (5 - 1) / 2
            # Calculate the x position of the bar
            x_position = offset[i] + group_width / 2 + distance_from_center * (bar_width)
            x.append(x_position)
        # Plot bars
        ax.bar(x, test_errors, bar_width, color=colors)

    # Set x-axis ticks and labels
    ax.set_xticks(offset + group_width / 2)
    ax.set_xticklabels(['ONLINE', 'BATCH'])

    # Add labels and title
    ax.set_xlabel('Batch Size')
    ax.set_ylabel('Test Errors')
    ax.set_title('Non Linear (SIGMOID) - Test Error vs. Batch Size - Shuffled Data')
    # Set custom legend with labels
    handles = [plt.Rectangle((0,0),1,1, color=colors[i], ec="k") for i in range(len(colors))]
    ax.legend(handles, labels)
    ax.grid(axis='y')
    ax.set_axisbelow(True)
    ax.set_ylim(0, df['test_errors'].max() *1.2)
    # Show the plot
    plt.tight_layout()
    plt.show()

# plot_testing_error_vs_k_linear_ordered()
# plot_testing_error_vs_k_linear_shuffled()
# plot_testing_error_vs_k_non_linear_sigmoid_shuffled()
# plot_testing_error_vs_k_non_linear_sigmoid_ordered()
# plot_testing_error_vs_k_non_linear_tanh_shuffled()
# plot_testing_error_vs_k_non_linear_tanh_ordered()
# plot_testing_error_vs_epochs_non_linear_tanh_shuffled()
# plot_testing_error_vs_epochs_non_linear_sigmoid_shuffled()
# plot_testing_error_vs_beta_non_linear_tanh_shuffled()
# plot_testing_error_vs_beta_non_linear_sigmoid_shuffled()
# plot_testing_error_vs_learning_non_linear_sigmoid_shuffled()
# plot_testing_error_vs_batch_non_linear_sigmoid_shuffled()
plot_training_error_vs_epoch_linear()
plot_training_error_vs_epoch_non_linear_sigmoid()
plot_training_error_vs_epoch_non_linear_tanh()