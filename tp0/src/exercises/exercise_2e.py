import json
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import pandas as pd


CONFIG_FILE_PATH="src/config/2e_config.json"
POKEMON_JSON="pokemon.json"
OUTPUT_FILE_PATH="src/output/2e_results.csv"

factory = PokemonFactory(POKEMON_JSON)
with open(CONFIG_FILE_PATH, "r") as f:
      data = json.load(f)
      POKEBALLS = data["pokeball"]
      POKEMONS = data["pokemon"]
results = []

levels = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for pokemon_name in POKEMONS:
      for level in levels:
        for hp in range(1, 101):
                for status in StatusEffect:
                    for pokeball in POKEBALLS:
                            pokemon = factory.create(pokemon_name, level, status, hp/100)
                            for _ in range(100):
                                catch_result = attempt_catch(pokemon, pokeball)
                                results.append({"Pokemon" : pokemon_name, "Level" : level, "HP" : hp, "Status Effect" : status.name, "Pokeball" : pokeball, "Catch result" : catch_result[0]})

        


df = pd.DataFrame(results)
df.to_csv(OUTPUT_FILE_PATH, index=False)