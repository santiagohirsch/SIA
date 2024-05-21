import csv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from algorithms.Oja import Oja


def main():
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
    
    df = pd.DataFrame(DATA).astype(float)
    df = df.apply(lambda x: (x - x.mean()) / x.std(), axis=0)
    data = np.array(df.values.tolist())
    oja = Oja(len(data[0]), lambda x: np.random.uniform(0, 1))
    w = oja.train(data, 0.01, 1000)
    pc1 = np.dot(data, w * -1)
    pc1_index_bar_plot(pc1, COUNTRIES)

def pc1_index_bar_plot(pc1, countries):
    plt.figure(figsize=(10, 10))
    plt.bar(countries, pc1, color='skyblue')
    plt.xticks(rotation=45)
    plt.title('PC1 Index')
    plt.grid(axis='y')
    plt.show()

if __name__ == '__main__':
    main()

