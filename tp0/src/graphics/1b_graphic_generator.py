import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH="src/output/1b_results.csv"
CONFIG_FILE_PATH="src/config/1b_config.json"
ATTEMPTS=100


with open(CONFIG_FILE_PATH, "r") as f:
    data = json.load(f)
    POKEBALLS = data["pokeball"]
    POKEMONS = data["pokemon"]
    BASE_POKEBALL = data["base_pokeball"]

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

for pokeball in pokeballs:
    if pokeball != BASE_POKEBALL:
        base_probabilities = np.array(probabilities_per_pokeball[BASE_POKEBALL])
        pokeball_probabilities = np.array(probabilities_per_pokeball[pokeball])
        divider = base_probabilities != 0
        probabilities_per_pokeball[pokeball] = np.where(divider, pokeball_probabilities / base_probabilities, pokeball_probabilities*100)
        probabilities_per_pokeball[pokeball] = np.round(probabilities_per_pokeball[pokeball], 3)

del probabilities_per_pokeball[BASE_POKEBALL]

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



ax.set_ylabel('Capture Rate (%)')
ax.set_title('Average Capture Rate for each Pokeball relative to the base pokeball')
ax.set_xticks(x + width, pokemons)
ax.legend(loc='upper right', ncols=2)
max_value = max(max(measurement) for measurement in probabilities_per_pokeball.values())
ax.set_yticks(np.arange(0, max_value + 1.25, 0.25))
ax.set_axisbelow(True)
plt.grid(True, axis='y')
plt.show()