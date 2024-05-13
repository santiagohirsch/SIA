import pandas as pd
import matplotlib.pyplot as plt

metric_functions = {
    'F1',
    'recall',
    'precision',
    'accuracy'
}

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
