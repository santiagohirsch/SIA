import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_catches_by_hp_for_pokemon(df, pokemon_name):
    # Filter the results for the specified Pokémon
    pokemon_data = df[df["Pokemon"] == pokemon_name]

    pokemon_hp_stats = pokemon_data.groupby("HP").agg(
        Mean_Count=("Catch result", "mean"),
        Std_Err_Count=("Catch result", "sem")
    ).reset_index()

    pokemon_data["Capture Percentage"] = pokemon_data.groupby("HP")["Catch result"].transform("mean") * 100

    plt.figure(figsize=(10, 6))

    # Plotting the mean capture percentage
    plt.plot(pokemon_data["HP"], pokemon_data["Capture Percentage"], marker='o', linestyle='-', label="Mean Capture Percentage")

    plt.xlabel('Pokemon HP')
    plt.ylabel('Capture Percentage')
    plt.title(f'Capture Percentage for Pokemon {pokemon_name}')
    plt.grid(True)

    plt.show()

ruta_del_archivo = 'src/output/2b_results.csv'

df = pd.read_csv(ruta_del_archivo)
for pokemon in df["Pokemon"].unique():
    plot_catches_by_hp_for_pokemon(df, pokemon)
