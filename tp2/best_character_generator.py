from math import tanh
import numpy as np
from scipy.optimize import minimize, Bounds
from src.utils.class_utils import CHARACTER_TYPES


# Define the fitness function
def fitness_function(vars, h, att_pct, def_pct):
    a, p, f, r, v = vars
    ATT = (tanh(0.01 * a) + 0.6 * tanh(0.01 * p)) * (100 * tanh(0.01 * f)) * (0.5 - (3*h - 5)**4 + (3*h - 5)**2 + h/2)
    DEF = (tanh(0.01 * r) + 0.6 * tanh(0.01 * p)) * (100 * tanh(0.01 * v)) * (2 + (3*h - 5)**4 - (3*h - 5)**2 - h/2)
    return -att_pct * ATT - def_pct * DEF  # Minimizing negative fitness is equivalent to maximizing fitness

# Define constraint function
def constraint(vars):
    return sum(vars) - 150

# Initial guess
x0 = [30, 30, 30, 30, 30]  # You can change initial values accordingly

# Define bounds for variables
bounds = Bounds([0, 0, 0, 0, 0], [150, 150, 150, 150, 150])  # Bounds for each variable

# Define constraints
cons = {'type': 'eq', 'fun': constraint}

CHARACTER_PERCENTAGES = {
    'archer': (0.9, 0.1),
    'warrior': (0.6, 0.4),
    'defender': (0.1, 0.9),
    'spy': (0.8, 0.3),
}

best_fitness_per_character = {}
best_configuration_per_character = {}

for h in np.arange(1.3, 2.0, 0.1):
    for character in CHARACTER_TYPES:


        # Perform optimization
        result = minimize(fitness_function, x0, args=(h, CHARACTER_PERCENTAGES[character][0], CHARACTER_PERCENTAGES[character][1]), bounds=bounds, constraints=cons)

        # Extract results
        optimal_vars = result.x
        optimal_fitness = -result.fun

        # Update best fitness per character
        if character not in best_fitness_per_character or optimal_fitness > best_fitness_per_character[character]:
            best_fitness_per_character[character] = optimal_fitness
            best_configuration_per_character[character] = (optimal_vars, h)



print("Best fitness per character:")
for character, fitness in best_fitness_per_character.items():
    rounded_fitness = round(fitness, 2)
    print(f"Character: {character}, Best Fitness: {rounded_fitness}, Best Configuration: {best_configuration_per_character[character][0]}, h: {best_configuration_per_character[character][1]}")
    

