import pandas as pd

# Step 1: Read the CSV file into a pandas DataFrame
df = pd.read_csv('/Users/santiago/Desktop/ITBA/1C2024/SIA/SIA/tp2/output/replacement_method.csv')

# Step 2: Group the data by Character, Replacement, First Selection Method, and Second Selection Method
grouped = df.groupby(['Character', 'Replacement', 'First Selection Method', 'Second Selection Method'])

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
    replacement = row['Replacement']
    first_method = row['First Selection Method']
    second_method = row['Second Selection Method']
    best_average_fitness = row['Average Fitness']
    average_generation_count = row['Generation']
    
    # Check if average_generation_count is not zero to avoid division by zero
    if average_generation_count != 0:
        coefficient = 10 / average_generation_count + best_average_fitness
    else:
        coefficient = best_average_fitness
    
    coefficients.append(coefficient)


# Sort the results by coefficient
aggregated_data['Coefficient'] = coefficients
sorted_data = aggregated_data.sort_values(by='Coefficient', ascending=False)

# Group by Replacement, First Selection Method, and Second Selection Method and calculate average coefficient
grouped_data = sorted_data.groupby(['Replacement', 'First Selection Method', 'Second Selection Method']).agg({'Coefficient': 'mean'}).reset_index()

# Sort the grouped and averaged results by coefficient
sorted_grouped_data = grouped_data.sort_values(by='Coefficient', ascending=False)

# Print the sorted results
print("Sorted grouped and averaged results:")
for _, row in sorted_grouped_data.iterrows():
    replacement = row['Replacement']
    first_method = row['First Selection Method']
    second_method = row['Second Selection Method']
    average_coefficient = row['Coefficient']
    
    print(f"Replacement: {replacement}, First Selection Method: {first_method}, Second Selection Method: {second_method}, Average Coefficient: {average_coefficient}")