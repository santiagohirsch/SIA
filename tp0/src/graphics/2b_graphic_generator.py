import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_catches_by_hp_for_pokemon(df, pokemon_name, ax):
    # Filter the results for the specified Pokémon
    pokemon_data = df[df["Pokemon"] == pokemon_name]

    # Calculate the mean capture percentage for each HP
    pokemon_data["Capture Percentage"] = pokemon_data.groupby("HP")["Catch result"].transform("mean") * 100

    # Plotting the mean capture percentage
    ax.plot(pokemon_data["HP"], pokemon_data["Capture Percentage"], marker='o', linestyle='-', label=pokemon_name)


def graphic_generator():
    ruta_del_archivo = 'src/output/2b_results.csv'
    df = pd.read_csv(ruta_del_archivo)

    # Create a single plot for all Pokémon
    plt.figure(figsize=(12, 8))
    ax = plt.gca()

    # Loop through each unique Pokémon and plot its data
    for pokemon in df["Pokemon"].unique():
        plot_catches_by_hp_for_pokemon(df, pokemon, ax)

    # Customize the plot
    plt.xlabel('Pokemon HP')
    plt.ylabel('Capture Rate (%)')
    plt.yticks(np.arange(0, 21, 1))
    plt.title('Capture Rate based on HP')
    plt.legend()
    plt.grid(True)

    plt.show()