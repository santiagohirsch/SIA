import json
import matplotlib.pyplot as plt

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import pandas as pd

ATTEMPS=100
POKEMON_JSON="pokemon.json"
CONFIG_FILE_PATH="src/config/2a_config.json"

def exercise():
    factory = PokemonFactory(POKEMON_JSON)
    catch_per_status = []
    status_names = []
    with open(CONFIG_FILE_PATH, "r") as f:
            data = json.load(f)
            POKEMON = data["pokemon"]
            POKEBALL = data["pokeball"]
    for status in StatusEffect:
        jolteon = factory.create(POKEMON, 100, status, 1.0) 
        count = 0
        for _ in range(1000):
            catch, _ = attempt_catch(jolteon, POKEBALL)
            if catch:
                count += 1
        catch_per_status.append(count)
        if status != StatusEffect.NONE:
            status_names.append(status.name)

    normalized_counts = [count / catch_per_status[-1] for count in catch_per_status]

    del normalized_counts[-1]

    ax = plt.gca()
    ax.set_axisbelow(True)
    plt.grid(True, axis='y')
    plt.bar(status_names, normalized_counts)
    for i, count in enumerate(normalized_counts):
        plt.text(i, count, f'{count:.2f}', ha='center', va='bottom', fontsize=10)
    plt.xlabel('Status Effect')
    plt.ylabel('Catch Ratio')
    plt.title('Catch Ratio for Different Status Effects on Jolteon')
    plt.show()