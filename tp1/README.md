
# TP1 SIA - Métodos de Búsqueda

## Introducción

Trabajo práctico n°1 para la materia Sistemas de Inteligencia Artificial.

[Enunciado](docs/SIA_TP1.pdf)

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

```
pipenv run python main.py -m [path_to_map] -a [algorithm_name]
```

Para correr el programa, se debe ejecutar el `main` como se indica, pasándole dos argumentos, sin importar el orden:

- `-m` o `--map`: Este parámetro acepta una ruta a uno de los mapas que se encuentran en la carpeta `./maps`.
- `-a` o `--algorithm`: Este parámetro acepta el nombre de uno de los algoritmos implementados. La lista de algoritmos implementados es:
  - AStar
  - BFS
  - DFS
  - LocalGreedy
  - GlobalGreedy