import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los Pokémon del archivo config.json
import json
with open('src/config/2c_config.json') as f:
    config_data = json.load(f)
    pokemon = config_data['pokemon']

df = pd.read_csv('src/output/2c_results.csv')

# Verificar si el DataFrame no está vacío
if not df.empty:
    # Agrupar por 'Pokemon', 'HP', 'Status Effect' y 'Pokeball' y contar el número de ocurrencias
    successful_catches = df[df['Catch result'] == True]
    grouped = successful_catches.groupby(['Level', 'HP', 'Status Effect', 'Pokeball']).size().reset_index(name='Successful Catches')

    # Combinar las columnas 'Pokemon', 'HP', 'Status Effect' y 'Pokeball' en una sola columna
    grouped['Pokemon Details'] =  "Pokemon: " + pokemon + ", Level: " + grouped["Level"].astype(str) + ", HP: " + grouped['HP'].astype(str) + ", Status Effect: " + grouped['Status Effect'] + ", Pokeball: " + grouped['Pokeball']

    # Graficar el top 5 para cada Pokémon
    plt.figure(figsize=(12, 6))
    ax = plt.gca()


    rects = ax.bar(grouped['Pokemon Details'], grouped['Successful Catches'], label=pokemon)
    ax.bar_label(rects, padding=3)

    ax.set_ylabel("Capture Rate (%)")
    ax.set_yticks(np.arange(0, 101, 5))
    ax.set_xlabel("Pokemon Details")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', wrap=True)
    ax.legend()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')
    plt.title("Top 5 combinations for each Pokemon")
    plt.tight_layout()
    plt.show()
else:
    print("El DataFrame está vacío. No hay datos para graficar.")
