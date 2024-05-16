from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def pca():
    # Ruta del archivo europe.csv
    archivo_csv = '../data/europe.csv'

    HEADER = []
    DATA = []
    COUNTRIES = []

    with open(archivo_csv, 'r') as f:
        reader = csv.reader(f)
        HEADER = next(reader)
        for row in reader:
            COUNTRIES.append(row[0])
            DATA.append(row[1:])

    scaler = StandardScaler()
    data = scaler.fit_transform(DATA)

    pca = PCA(n_components=7)
    pca_fitted = pca.fit(data)
    fitted_data = pca_fitted.transform(data)
    load_vector = pca.components_
    load_vector = load_vector/np.linalg.norm(load_vector, axis=1)[:, np.newaxis]
    bi_plot(fitted_data, COUNTRIES, load_vector, HEADER[1:])

    


def bi_plot(fitted_data, countries, load_vector, vars):
    df =  pd.DataFrame(fitted_data, columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7'])
    df['Country'] = countries
    plt.figure(figsize=(10, 10))
    plt.scatter(df['PC1'], df['PC2'], s=100)
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('Biplot')
    for i, txt in enumerate(countries):
        plt.annotate(txt, (df['PC1'][i], df['PC2'][i]))

    scale = 3
    for i, txt in enumerate(vars):
        plt.arrow(0, 0, load_vector[0][i] * scale, load_vector[1][i] * scale, color='r', alpha=0.5)
        plt.text(load_vector[0][i] * scale, load_vector[1][i] * scale, txt, color='r', ha='center', va='center')

    plt.grid()
    plt.show()



pca()