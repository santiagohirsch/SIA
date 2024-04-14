import csv
def get_average_fitness_per_method(file_path):
    best_fitness = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        first_line = next(reader)
        best_partial_fitness = 0
        best_fitness_per_method = []
        generation_count = []
        generation_count_per_method = []
        partial_method = first_line[1]
        generation_aux = 0
        for row in reader:
            if partial_method != str(row[1]):
                best_fitness.append(best_fitness_per_method)
                best_fitness_per_method = []
                generation_count.append(generation_count_per_method)
                partial_method = str(row[1])
            fitness = float(row[4])
            if fitness > best_partial_fitness:
                best_partial_fitness = fitness
            if int(row[2]) == 0:
                best_fitness_per_method.append(best_partial_fitness)
                best_partial_fitness = 0
                generation_count_per_method.append(generation_aux)
                generation_aux = 0
            generation_aux = generation_aux + 1

        best_fitness.append(best_fitness_per_method)
        generation_count.append(generation_count_per_method)
        toReturn = [] 
        generation_avg = []
        for array in best_fitness:
            toReturn.append(sum(array)/len(array))
        for array in generation_count:
            generation_avg.append(sum(array)/len(array))
        return toReturn, generation_avg


file_path = '/Users/santiago/Desktop/ITBA/1C2024/SIA/SIA/tp2/output/crossing_method.csv'
avg_fitness, generation_avg = get_average_fitness_per_method(file_path)
one_point = 0.0
two_point = 0.0
uniform = 0.0
anular = 0.0
coefficient = 0.0
print("the order is 1-point, 2-point, uniform, anular")
for i in range(0,4):
    coefficient = 10/generation_avg[i] + avg_fitness[i]
    print("Average fitness for archer are", i, ":", avg_fitness[i])
    print("Coefficient: ", coefficient)
    if i % 4 == 0:
        one_point = one_point + coefficient
    elif i % 4 == 1:
        two_point = two_point + coefficient
    elif i % 4 == 2:
        uniform = uniform + coefficient
    elif i % 4 == 3:
        anular = anular + coefficient
for i in range(4,8):
    coefficient = 10/generation_avg[i] + avg_fitness[i]
    print("Average fitness for warriors are", i, ":", avg_fitness[i])
    print("Coefficient: ", coefficient)
    if i % 4 == 0:
        one_point = one_point + coefficient
    elif i % 4 == 1:
        two_point = two_point + coefficient
    elif i % 4 == 2:
        uniform = uniform + coefficient
    elif i % 4 == 3:
        anular = anular + coefficient
for i in range(8,12):
    coefficient = 10/generation_avg[i] + avg_fitness[i]
    print("Average fitness for defender are", i, ":", avg_fitness[i])
    print("Coefficient: ", coefficient)
    if i % 4 == 0:
        one_point = one_point + coefficient
    elif i % 4 == 1:
        two_point = two_point + coefficient
    elif i % 4 == 2:
        uniform = uniform + coefficient
    elif i % 4 == 3:
        anular = anular + coefficient
for i in range(12,16):
    coefficient = 10/generation_avg[i] + avg_fitness[i]
    print("Average fitness for spy are", i, ":", avg_fitness[i])
    print("Coefficient: ", coefficient)
    if i % 4 == 0:
        one_point = one_point + coefficient
    elif i % 4 == 1:
        two_point = two_point + coefficient
    elif i % 4 == 2:
        uniform = uniform + coefficient
    elif i % 4 == 3:
        anular = anular + coefficient

print("Average coefficient for one point is: ", one_point/4)
print("Average coefficient for two point is: ", two_point/4)
print("Average coefficient for uniform is: ", uniform/4)
print("Average coefficient for anular is: ", anular/4)
