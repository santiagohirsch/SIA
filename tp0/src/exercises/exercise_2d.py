import json
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import pandas as pd


CONFIG_FILE_PATH="src/config/2d_config.json"
POKEMON_JSON="pokemon.json"
OUTPUT_FILE_PATH="src/output/2d_results.csv"

def exercise():
      factory = PokemonFactory(POKEMON_JSON)
      with open(CONFIG_FILE_PATH, "r") as f:
            data = json.load(f)
            POKEBALLS = data["pokeball"]
            POKEMONS = data["pokemon"]
      results = []

      for pokemon_name in POKEMONS:
            for hp in range(1, 101):
                  for status in StatusEffect:
                        for pokeball in POKEBALLS:
                              pokemon = factory.create(pokemon_name, 100, status, hp/100)
                              for _ in range(100):
                                    catch_result = attempt_catch(pokemon, pokeball)
                                    results.append({"Pokemon" : pokemon_name, "HP" : hp, "Status Effect" : status.name, "Pokeball" : pokeball, "Catch result" : catch_result[0]})

            


      df = pd.DataFrame(results)
      df.to_csv(OUTPUT_FILE_PATH, index=False)