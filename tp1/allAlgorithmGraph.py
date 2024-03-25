import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('results2.csv')

# Asegúrate de que 'Algorithm' y 'Duration' están en tus columnas
assert 'Algorithm' in df.columns, "La columna 'Algorithm' no se encuentra en el CSV"
assert 'Duration' in df.columns, "La columna 'Duration' no se encuentra en el CSV"

# df2 = df[df['Algorithm'] == 'iddfs']
df = df[df['Algorithm'] != 'iddfs']
df = df[df['Heuristic'] == 'manhattan']



grouped = df.groupby('Algorithm')['Duration'].mean()
std_dev = df.groupby('Algorithm')['Duration'].std()

grouped.rename(index={'localgreedy': 'Local Greedy'}, inplace=True)
std_dev.rename(index={'localgreedy': 'Local Greedy'}, inplace=True)

grouped.rename(index={'globalgreedy': 'Global Greedy'}, inplace=True)
std_dev.rename(index={'globalgreedy': 'Global Greedy'}, inplace=True)

grouped.rename(index={'astar': 'A*'}, inplace=True)
std_dev.rename(index={'astar': 'A*'}, inplace=True)

grouped.rename(index={'bfs': 'BFS'}, inplace=True)
std_dev.rename(index={'bfs': 'BFS'}, inplace=True)

grouped.rename(index={'dfs': 'DFS'}, inplace=True)
std_dev.rename(index={'dfs': 'DFS'}, inplace=True)

grouped.rename(index={'iddfs': 'IDDFS'}, inplace=True)
std_dev.rename(index={'iddfs': 'IDDFS'}, inplace=True)

grouped.plot(kind='bar', yerr=std_dev)
grouped.plot(kind='bar')

bar = plt.bar(grouped.index, grouped, yerr=std_dev, color=['b', 'g', 'r', 'c', 'm', 'y', 'k'])


for i in range(len(grouped)):
    plt.text(i, grouped[i]+ std_dev[i] + 0.0002, round(grouped[i], 6), ha = 'center')



plt.xlabel('Algorithm')
plt.ylabel('Average Duration')
plt.title('Comparison of Algorithm Duration')

plt.xticks(rotation=0)

# Mostrar el gráfico
plt.show()


# iddfs = df2.groupby('Heuristic')['Duration'].mean()
# iddfs_std = df2.groupby('Heuristic')['Duration'].std()


# # iddfs.rename(index={'manhattan': 'Manhattan'}, inplace=True)
# # iddfs_std.rename(index={'manhattan': 'Manhattan'}, inplace=True)

# # iddfs.rename(index={'improvedman': 'Improved Manhattan'}, inplace=True)
# # iddfs_std.rename(index={'improvedman': 'Improved Manhattan'}, inplace=True)


# iddfs.plot(kind='bar', yerr=iddfs_std)
# iddfs.plot(kind='bar')

# plt.xlabel('IDDFS')
# plt.ylabel('Average Duration')
# plt.title('IDDFS average Duration')

# plt.xticks(rotation=0)


# plt.show()

