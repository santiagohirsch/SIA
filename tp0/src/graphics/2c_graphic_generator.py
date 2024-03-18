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

    # Combinar las columnas 'Pokemon', 'HP', 'Status Effect' y 'Pokeball' en una sola columna
    # Only include the attributes that have been changed from the default values
    # Check if all values are default
    default_values = {'Level': 100, 'HP': 100, 'Status Effect': 'NONE', 'Pokeball': 'pokeball'}


    grouped['Pokemon Details'] = grouped.apply(lambda row: ", ".join([f"{attr}: {row[attr]}" for attr in default_values if row[attr] != default_values[attr]]) if any(row[attr] != default_values[attr] for attr in default_values) else 'Default', axis=1)

    grouped = grouped.sort_values(by='Pokemon Details', key=lambda x: x != 'Default')
    plt.figure(figsize=(12, 6))
    ax = plt.gca()
    rects = ax.bar(grouped['Pokemon Details'], grouped['Successful Catches'], label=pokemon)
    ax.bar_label(rects, padding=3)

    ax.set_ylabel("Capture Rate (%)")
    ax.set_yticks(np.arange(0, 101, 5))
    ax.set_xlabel("Changed Attributes")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', wrap=True)
    ax.legend()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')
    plt.title("Capture Rate for each combination of changed attributes")
    plt.tight_layout()
    plt.show()

    # rects = ax.bar(grouped['Pokemon Details'], grouped['Successful Catches'], label=pokemon)
    # ax.bar_label(rects, padding=3)

    # ax.set_ylabel("Capture Rate (%)")
    # ax.set_yticks(np.arange(0, 101, 5))
    # ax.set_xlabel("Pokemon Details")
    # ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', wrap=True)
    # ax.legend()
    # ax.set_axisbelow(True)
    # plt.grid(True, axis='y')
    # plt.title("Top 5 combinations for each Pokemon")
    # plt.tight_layout()
    # plt.show()
else:
    print("El DataFrame está vacío. No hay datos para graficar.")
