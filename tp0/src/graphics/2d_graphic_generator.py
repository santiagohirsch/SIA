import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los Pokémon del archivo config.json
import json

def graphic_generator():
    with open('src/config/2d_config.json') as f:
        config_data = json.load(f)
    pokemon_list = config_data["pokemon"]

    df = pd.read_csv('src/output/2d_results.csv')

    # Verificar si el DataFrame no está vacío
    if not df.empty:
        # Filtrar los Pokémon de interés
        filtered_df = df[df['Pokemon'].isin(pokemon_list) & (df['Catch result'] == True)]

        # Verificar si el DataFrame filtrado no está vacío
        if not filtered_df.empty:
            # Agrupar por 'Pokemon', 'HP', 'Status Effect' y 'Pokeball' y contar el número de ocurrencias
            grouped = filtered_df.groupby(['Pokemon', 'HP', 'Status Effect', 'Pokeball']).size().reset_index(name='Successful Catches')

            # Combinar las columnas 'Pokemon', 'HP', 'Status Effect' y 'Pokeball' en una sola columna
            grouped['Pokemon Details'] =  grouped['Pokemon'] + ", HP: " + grouped['HP'].astype(str) + ", Status Effect: " + grouped['Status Effect'] + ", Pokeball: " + grouped['Pokeball']

            # Graficar el top 5 para cada Pokémon
            plt.figure(figsize=(12, 6))
            ax = plt.gca()
            for pokemon in pokemon_list:
                pokemon_data = grouped[grouped['Pokemon'] == pokemon]
                if not pokemon_data.empty:
                    top_5_pokemon_data = pokemon_data.sort_values('Successful Catches', ascending=False).head(5)
                    rects = ax.bar(top_5_pokemon_data['Pokemon Details'], top_5_pokemon_data['Successful Catches'], label=pokemon)
                    ax.bar_label(rects, padding=3)

            # x_spacing = 1.3
            # x = np.linspace(0, (len(pokemon_list) - 1) * x_spacing, len(pokemon_list))
            # width = 0.25
            # multiplier = 0

            # fig, ax = plt.subplots(layout='constrained')

            # for attribute, measurement in top_5_pokemon_data.items():

            #     offset = width * multiplier
            #     rects = ax.bar(x + offset, measurement, width, label=attribute)
            #     ax.bar_label(rects, padding=3)
            #     multiplier += 1

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
            print("No hay resultados exitosos para los Pokémon especificados en config.json.")
    else:
        print("El DataFrame está vacío. No hay datos para graficar.")
