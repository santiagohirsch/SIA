import json
import sys
import importlib

if __name__ == "__main__":
    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)
        exercisePath = config["exercise_path"]
        graphic_generator = config["graphic_generator_path"]
    try:
        exercise = importlib.import_module(f"src.exercises.{exercisePath}")
        graphic_generator = importlib.import_module(f"src.graphics.{graphic_generator}")
    except ModuleNotFoundError:
        print(f"Ha ocurrido un error al importar el módulo {exercisePath} o {graphic_generator}")
        sys.exit(1)
    
    exercise.exercise()
    graphic_generator.graphic_generator()
        