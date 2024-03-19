import json
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import pandas as pd

ATTEMPS=100
POKEMON_JSON="pokemon.json"
CONFIG_FILE_PATH="src/config/2a_config.json"
OUTPUT_FILE_PATH="src/output/2a_results.csv"

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

    # Crear un DataFrame con los datos analizados
    data = {
        'Status Effect': status_names,
        'Catch Ratio': normalized_counts
    }
    df = pd.DataFrame(data)

    # Guardar el DataFrame en un archivo CSV
    df.to_csv(OUTPUT_FILE_PATH, index=False)