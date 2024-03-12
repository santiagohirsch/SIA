import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH="../output/1a_results.csv"
ATTEMPTS=100

csv = pd.read_csv(CSV_PATH)
pokeballs = csv["Pokeball"].unique()
pokemons = csv["Pokemon"].unique()

probabilities_per_pokeball = {}

for pokeball in pokeballs:
    probabilities_per_pokeball[pokeball] = ()

for pokemon_name in pokemons:
    for pokeball in pokeballs:
        pokemon_info = csv[csv["Pokemon"] == pokemon_name]
        pokeball_info = pokemon_info[pokemon_info["Pokeball"] == pokeball]
        results = pokeball_info[pokeball_info["Catch result"] == True]
        probabilities_per_pokeball[pokeball] += (len(results)/ATTEMPTS,)


x_spacing = 1.3
x = np.linspace(0, (len(pokemons) - 1) * x_spacing, len(pokemons))
width = 0.25
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in probabilities_per_pokeball.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_ylabel('Capture rate')
ax.set_title('Average Capture rate for each Pokeball')
ax.set_xticks(x + width, pokemons)
ax.legend(loc='upper right', ncols=2)
ax.set_ylim(0, 1)

plt.show()