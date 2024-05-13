import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def exercise_3c():
    data = pd.read_csv('all_errors.csv')
    iterations = data['Index']
    errors = data['Error']
    
    plt.plot(iterations, errors)
    plt.grid()
    plt.yticks(range(int(min(errors)), int(max(errors))+1, 1))
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.title('Error by Epoch in XOR Function')
    plt.show()

def betas_graph():
    data = pd.read_csv('betas1.csv')

    # Lista para almacenar todos los DataFrames adicionales
    additional_dfs = []

    # Leer y agregar los siguientes archivos CSV a la lista
    additional_dfs.append(pd.read_csv('betas01.csv'))
    additional_dfs.append(pd.read_csv('betas025.csv'))
    additional_dfs.append(pd.read_csv('betas05.csv'))
    additional_dfs.append(pd.read_csv('betas2.csv'))
    additional_dfs.append(pd.read_csv('betas3.csv'))
    additional_dfs.append(pd.read_csv('betas4.csv'))

    # Concatenar todos los DataFrames en la lista en uno solo
    data = pd.concat([data] + additional_dfs, ignore_index=True)
    
    grouped_data = data.groupby('Beta')
    for beta, group in grouped_data:
        plt.plot(group['Index'], group['Error'], label=f'Beta = {beta}')
    
    plt.grid()
    plt.yticks(range(int(min(data['Error'])), int(max(data['Error']))+1, 1))
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.title('Error by Epoch for Different Beta Values')
    plt.legend()
    plt.show()

def learning_rate_graph():
    data = pd.read_csv('lr01.csv')

    # Lista para almacenar todos los DataFrames adicionales
    additional_dfs = []

    # Leer y agregar los siguientes archivos CSV a la lista
    additional_dfs.append(pd.read_csv('lr001.csv'))
    additional_dfs.append(pd.read_csv('lr0001.csv'))

    # Concatenar todos los DataFrames en la lista en uno solo
    data = pd.concat([data] + additional_dfs, ignore_index=True)

    grouped_data = data.groupby('Learning Rate')
    for lr, group in grouped_data:
        plt.plot(group['Index'], group['Error'], label=f'Learning Rate = {lr}')
    
    plt.grid()
    plt.yticks(range(int(min(data['Error'])), int(max(data['Error']))+1, 1))
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.title('Error by Epoch for Different Learning Rates')
    plt.legend()
    plt.show()


exercise_3c()