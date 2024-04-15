
# TP2 SIA - Algoritmos Genéricos

## Introducción

Trabajo práctico n°2 para la materia Sistemas de Inteligencia Artificial.

[Enunciado](docs/SIA_TP2.pdf)

### Requisitos

- Python3
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

```sh
pipenv install
```

para instalar las dependencias necesarias en el ambiente virtual

## Ejecución

Todas los archivos de salida se guardan en la carpeta `output`
Para ejecutar el proyecto, sigue estos pasos:

1. **Crear archivo de configuración**: Este comando creará un archivo de configuracion llamado `config.json`. Dentro del mismo se deberá elegir, a partir de las [opciones proporcionadas](#opciones-de-configuración), la configuracion con la que se ejecutará el codigo.
    ```sh
    make create_config
    ```

2. **Ejecutar el algoritmo**: Este comando ejecutará el algoritmo principal utilizando la configuración especificada y guardará la salida en un archivo de texto llamado.
    ```sh
    make run
    ```

### Opciones de configuración

Las siguientes son las opciones de configuracion como aparecen en el archivo `config_options.json`:

```json
{
    "character": "[ archer | defender | spy | warrior ]",
    "attribute_sets": [
        {"agility": 15, "strength":  25, "expertise": 35, "endurance": 40, "health": 35, "height": 1.6 },
        {"agility": 20, "strength":  30, "expertise": 30, "endurance": 35, "health": 35, "height": 1.5 },
        {"agility": 25, "strength":  35, "expertise": 25, "endurance": 30, "health": 35, "height": 1.7 },
        {"agility": 30, "strength":  40, "expertise": 20, "endurance": 25, "health": 35, "height": 1.8 },
        {"agility": 35, "strength":  45, "expertise": 15, "endurance": 20, "health": 35, "height": 2.0 },
        {"agility": 40, "strength":  50, "expertise": 10, "endurance": 15, "health": 35, "height": 1.3 },
        {"agility": 45, "strength":  55, "expertise": 5, "endurance": 10, "health": 35, "height": 1.9 },
        {"agility": 50, "strength":  60, "expertise": 0, "endurance": 5, "health": 35, "height": 1.4 },
        {"agility": 55, "strength":  55, "expertise": 5, "endurance": 5, "health": 30, "height": 1.6 },
        {"agility": 60, "strength":  50, "expertise": 10, "endurance": 5, "health": 25, "height": 1.8 }
    ],
    "crossing": "[ annular | one_point | two_point | uniform ]",
    "mutation": {
        "name": "[ single | uniform | limited | complete ]",
        "rate": "[ 0.0 - 1.0 ]"
    },
    "selection": {

        "first": {
            "name": "[ roulette | elite | universal | tournament_det | tournament_prob | ranking | boltzmann ]",
            "params": "[tournament_det: {\"range\":  2} | boltzmann {\"T0\": 10, \"TC\": 5, \"k\": 2, \"generation\": 10} | else: {} ]"
        },
        "second": {
            "name": "[ roulette | elite | universal | tournament_det | tournament_prob | ranking | boltzmann ]",
            "params": "[tournament_det: {\"range\":  2} | boltzmann {\"T0\": 10, \"TC\": 5, \"k\": 2, \"generation\": 10} | else: {} ]"
        },
        "a_value": "[ 0.0 - 1.0 ]"
    },
    "individuals": "[ > 0 ]",
    "cutoff": {
        "name": "[ content | structure | max_gen | optimum ]",
        "value": "[structure: [ 0.0 - 1.0 ] | else: > 0 ]",
        "generations": "[ structure: > 0 | else : 0 ]"
    },
    "replacement": {
        "name": "[ traditional | young ]",
        "b_value": "[ 0.0 - 1.0 ]",
        "selection": {
            "first": {
                "name": "[ roulette | elite | universal | tournament_det | tournament_prob | ranking | boltzmann ]",
                "params": "[tournament_det: {\"range\":  2} | boltzmann {\"T0\": 10, \"TC\": 5, \"k\": 2, \"generation\": 10} | else: {} ]"
            },
            "second": {
                "name": "[ roulette | elite | universal | tournament_det | tournament_prob | ranking | boltzmann ]",
                "params": "[tournament_det: {\"range\":  2} | boltzmann {\"T0\": 10, \"TC\": 5, \"k\": 2, \"generation\": 10} | else: {} ]"
            }
        }
    }
    
}
```