import json
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import pandas as pd


CONFIG_FILE_PATH="src/config/2c_config.json"
POKEMON_JSON="pokemon.json"
OUTPUT_FILE_PATH="src/output/2c_results.csv"

def exercise():
    factory = PokemonFactory(POKEMON_JSON)
    with open(CONFIG_FILE_PATH, "r") as f:
        data = json.load(f)
        POKEMON = data["pokemon"]
        BASE_POKEBALL = data["base_pokeball"]
        ALT_POKEBALL = data["alternative_pokeball"]
        ALT_LEVEL = data["alternative_level"]
        ALT_HP = data["alternative_hp"]
        ALT_STATUS = data["alternative_status"]
    results = []


    ORIGINAL_HP = 1
    HP_PERCENTAGE = 100


    # Default loop
    pokemon = factory.create(POKEMON, 100, StatusEffect.NONE, ORIGINAL_HP)
    print(pokemon)
    for _ in range(100):
        catch_result = attempt_catch(pokemon, BASE_POKEBALL)
        results.append({"Pokemon" : POKEMON, "Level" : pokemon.level, "HP" : HP_PERCENTAGE, "Status Effect" : pokemon.status_effect.name, "Pokeball" : BASE_POKEBALL, "Catch result" : catch_result[0]})
    # Loop with alternative pokeball
    for _ in range(100):
        catch_result = attempt_catch(pokemon, ALT_POKEBALL)
        results.append({"Pokemon" : POKEMON, "Level" : pokemon.level, "HP" : HP_PERCENTAGE, "Status Effect" : pokemon.status_effect.name, "Pokeball" : ALT_POKEBALL, "Catch result" : catch_result[0]})
    # Loop with alternative level
    pokemon_alt_level = factory.create(POKEMON, ALT_LEVEL, StatusEffect.NONE, 1)
    for _ in range(100):
        catch_result = attempt_catch(pokemon_alt_level, BASE_POKEBALL)
        results.append({"Pokemon" : POKEMON, "Level" : ALT_LEVEL, "HP" : HP_PERCENTAGE, "Status Effect" : pokemon_alt_level.status_effect.name, "Pokeball" : BASE_POKEBALL, "Catch result" : catch_result[0]})
    # Loop with alternative HP
    pokemon_alt_hp = factory.create(POKEMON, 100, StatusEffect.NONE, ALT_HP/100)
    for _ in range(100):
        catch_result = attempt_catch(pokemon_alt_hp, BASE_POKEBALL)
        results.append({"Pokemon" : POKEMON, "Level" : pokemon_alt_hp.level, "HP" : ALT_HP, "Status Effect" : pokemon_alt_hp.status_effect.name, "Pokeball" : BASE_POKEBALL, "Catch result" : catch_result[0]})
    # Loop with alternative status
    pokemon_alt_status = factory.create(POKEMON, 100, StatusEffect[ALT_STATUS], 1)
    for _ in range(100):
        catch_result = attempt_catch(pokemon_alt_status, BASE_POKEBALL)
        results.append({"Pokemon" : POKEMON, "Level" : pokemon_alt_status.level, "HP" : HP_PERCENTAGE, "Status Effect" : ALT_STATUS, "Pokeball" : BASE_POKEBALL, "Catch result" : catch_result[0]})
        


    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_FILE_PATH, index=False)

