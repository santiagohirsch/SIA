import json
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import pandas as pd
import numpy as np


CONFIG_FILE_PATH="src/config/2b_config.json"
POKEMON_JSON="pokemon.json"
OUTPUT_FILE_PATH="src/output/2b_results.csv"

factory = PokemonFactory(POKEMON_JSON)
with open(CONFIG_FILE_PATH, "r") as f:
      data = json.load(f)
      POKEBALL = data["pokeball"]
      POKEMONS = data["pokemon"]
results = []

for pokemon_name in POKEMONS:
    for hp in range(1, 100):
      pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, hp/100)
      for _ in range(1000):
        catch_result = attempt_catch(pokemon, POKEBALL)
        results.append({"Pokemon" : pokemon_name, "HP" : hp, "Catch result" : catch_result[0]})


df = pd.DataFrame(results)
df.to_csv(OUTPUT_FILE_PATH, index=False)