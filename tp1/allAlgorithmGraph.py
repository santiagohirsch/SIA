import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('results.csv')

# Asegúrate de que 'Algorithm' y 'Duration' están en tus columnas
assert 'Algorithm' in df.columns, "La columna 'Algorithm' no se encuentra en el CSV"
assert 'Duration' in df.columns, "La columna 'Duration' no se encuentra en el CSV"

df2 = df[df['Algorithm'] == 'iddfs']
df = df[df['Algorithm'] != 'iddfs']


grouped = df.groupby('Algorithm')['Duration'].mean()
std_dev = df.groupby('Algorithm')['Duration'].std()

iddfs = df2['Duration'].mean()
iddfs_std = df2['Duration'].std()

grouped.plot(kind='bar', yerr=std_dev)
grouped.plot(kind='bar')

plt.xlabel('Algorithm')
plt.ylabel('Average Duration')
plt.title('Comparison of Algorithm Durations')

# Mostrar el gráfico
plt.show()


iddfs.plot(kind='bar', yerr=iddfs_std)
iddfs.plot(kind='bar')

plt.xlabel('IDDFS')
plt.ylabel('Average Duration')
plt.title('IDDFS average duration')

plt.show()

