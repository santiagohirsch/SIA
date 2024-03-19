import matplotlib.pyplot as plt
import pandas as pd

CSV_PATH="src/output/2a_results.csv"

def graphic_generator():
    # Leer el archivo CSV
    df = pd.read_csv(CSV_PATH)

    # Crear el gráfico
    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')
    plt.bar(df['Status Effect'], df['Catch Ratio'])
    for i, count in enumerate(df['Catch Ratio']):
        plt.text(i, count, f'{count:.2f}', ha='center', va='bottom', fontsize=10)
    plt.xlabel('Status Effect')
    plt.ylabel('Catch Ratio')
    plt.title('Catch Ratio for Different Status Effects on Jolteon')
    plt.show()