import json
import sys
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import pandas as pd

if __name__ == "__main__":
    
    CONFIG_FILE_PATH="config/1a_config.json"
    POKEMON_JSON="pokemon.json"
    OUTPUT_FILE_PATH="output/1a_results.csv"

    factory = PokemonFactory(POKEMON_JSON)
    with open(CONFIG_FILE_PATH, "r") as f:
            data = json.load(f)
            POKEBALLS = data["pokeball"]
            POKEMONS = data["pokemon"]
    results = []

    for pokemon_name in POKEMONS:
        pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)
        for pokeball in POKEBALLS:
            for _ in range(100):
                    catch_result = attempt_catch(pokemon, pokeball)
                    results.append({"Pokemon" : pokemon_name, "Pokeball" : pokeball, "Catch result" : catch_result[0]})


    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_FILE_PATH, index=False)