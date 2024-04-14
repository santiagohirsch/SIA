import pandas as pd

# Step 1: Read the CSV file into a pandas DataFrame
df = pd.read_csv("/Users/santiago/Desktop/ITBA/1C2024/SIA/SIA/tp2/output/mutation_method.csv")

# Step 2: Group the data by Character, Mutation Method, and Mutation Rate
grouped = df.groupby(['Character', 'Mutation Method', 'Mutation Rate'])

# Step 3: Aggregate the data to calculate the best average fitness and average generation count
aggregated_data = grouped.agg({
    'Best Fitness': 'max',
    'Average Fitness': 'mean',
    'Generation': 'mean'
}).reset_index()

# Step 4: Iterate over unique combinations to retrieve the desired information and calculate the coefficient
coefficients = []
for _, row in aggregated_data.iterrows():
    character = row['Character']
    mutation_method = row['Mutation Method']
    mutation_rate = row['Mutation Rate']
    best_average_fitness = row['Average Fitness']
    average_generation_count = row['Generation']
    
    coefficient = 10 / average_generation_count + best_average_fitness
    coefficients.append(coefficient)
    

# Sort the results by coefficient
aggregated_data['Coefficient'] = coefficients
sorted_data = aggregated_data.sort_values(by='Coefficient', ascending=False)

# Group by Mutation Method and Mutation Rate and calculate average coefficient
grouped_data = sorted_data.groupby(['Mutation Method', 'Mutation Rate']).agg({'Coefficient': 'mean'}).reset_index()

# Sort the grouped and averaged results by coefficient
sorted_grouped_data = grouped_data.sort_values(by='Coefficient', ascending=False)

# Print the sorted results
print("Sorted grouped and averaged results:")
for _, row in sorted_grouped_data.iterrows():
    mutation_method = row['Mutation Method']
    mutation_rate = row['Mutation Rate']
    average_coefficient = row['Coefficient']
    
    print(f"Mutation Method: {mutation_method}, Mutation Rate: {mutation_rate}, Average Coefficient: {average_coefficient}")