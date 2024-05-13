import pandas as pd
import matplotlib.pyplot as plt

metric_functions = {
    'F1',
    'recall',
    'precision',
    'accuracy'
}

def graph_metrics_vs_epochs():
    for metric in metric_functions:
        # Crear un DataFrame desde el archivo CSV
        df = pd.read_csv(f"./{metric}-digits-nosplit-noise.csv")

        # Extraer los valores de epoch, training y test
        epoch = df['epoch']
        training = df['training']
        test = df['test']

        # Crear el gráfico
        plt.figure(figsize=(10, 6))

        # Dibujar los puntos de training y unirlos con una línea
        plt.plot(epoch, training, color='blue', marker='o', label='Training')

        # Dibujar los puntos de test y unirlos con una línea
        plt.plot(epoch, test, color='red', marker='o', label='Test')

        # Añadir etiquetas y título
        plt.xlabel('Epoch')
        plt.ylabel('Metrics')
        plt.title(f'Training and Test Metrics Over Epochs ({metric})')

        # Añadir leyenda
        plt.legend()

        # Mostrar el gráfico
        plt.grid(True)
        plt.show()

def graph_errors_vs_epochs_lr():
    plt.figure(figsize=(10, 6))
    for lr in [0.5, 0.3, 0.1, 0.01, 0.001]:
        # Crear un DataFrame desde el archivo CSV
        df = pd.read_csv(f"./lr_{lr}.csv")

        # Extraer los valores de epoch y error
        epoch = df['Epoch']
        error = df['Error']

        # Dibujar los puntos de error y unirlos con una línea
        plt.plot(epoch, error, marker='o', label=f'lr={lr}')

    # Añadir etiquetas y título
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.title('Error Over Epochs')

    # Añadir leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.grid(True)
    plt.show()

def graph_errors_vs_epochs_npl():
    plt.figure(figsize=(10, 6))
    for npl in ['35_10_10_10_10', '35_10_10_10', '35_10_10']:
        # Crear un DataFrame desde el archivo CSV
        df = pd.read_csv(f"./{npl}.csv")

        # Extraer los valores de epoch y error
        epoch = df['Epoch']
        error = df['Error']

        # Dibujar los puntos de error y unirlos con una línea
        plt.plot(epoch, error, marker='o', label=f'npl={npl}')

    # Añadir etiquetas y título
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.title(f'Error Over Epochs Neurons per Layer')

    # Añadir leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.grid(True)
    plt.show()

def graph_errors_vs_epochs_batch():
    plt.figure(figsize=(10, 6))
    # Crear un DataFrame desde el archivo CSV
    df = pd.read_csv(f"./batch_{1}.csv")

    # Extraer los valores de epoch y error
    epoch = df['Epoch']
    error = df['Error']

    # Dibujar los puntos de error y unirlos con una línea
    plt.plot(epoch, error, marker='o', label=f'batch={1}')


    df = pd.read_csv(f"./batch_{24}.csv")

    # Extraer los valores de epoch y error
    epoch = df['Epoch']
    error = df['Error']

    # Dibujar los puntos de error y unirlos con una línea
    plt.plot(epoch, error, marker='o', label=f'batch={24}')

    # Añadir etiquetas y título
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.title('Error Over Epochs batch')

    # Añadir leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.grid(True)
    plt.show()

def graphs_errors_vs_epochs_parity():
    plt.figure(figsize=(10, 6))
    # Crear un DataFrame desde el archivo CSV
    df = pd.read_csv(f"./parity.csv")

    # Extraer los valores de epoch y error
    epoch = df['Epoch']
    error = df['Error']

    # Dibujar los puntos de error y unirlos con una línea
    plt.plot(epoch, error, label=f'parity')

    # Añadir etiquetas y título
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.title('Error Over Epochs parity')

    # Añadir leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.grid(True)
    plt.show()

# graph_errors_vs_epochs_lr()
# graph_errors_vs_epochs_batch()
# graph_errors_vs_epochs_npl()
graphs_errors_vs_epochs_parity()