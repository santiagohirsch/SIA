import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('src/output/2d_results.csv')

# Check if the DataFrame is empty
if not df.empty:
    # Filter and group the data
    filtered_df = df[df['Catch result'] == True]
    grouped = filtered_df.groupby(['Pokemon', 'HP', 'Status Effect', 'Pokeball']).size()

    # Check if the grouped DataFrame is empty
    if not grouped.empty:
        # Convert the groupby object to a DataFrame
        grouped_df = grouped.reset_index(name='Successful Catches')

        # Sort the DataFrame by 'Successful Catches' in descending order and get the top 5
        top_5_grouped_df = grouped_df.sort_values('Successful Catches', ascending=False).head(5)

        # Combine the columns 'Pokemon', 'HP', 'Status Effect', and 'Pokeball' into a single column
        top_5_grouped_df['Pokemon Details'] =  top_5_grouped_df['Pokemon'] + " " + top_5_grouped_df['HP'].astype(str) + ", " + top_5_grouped_df['Status Effect'] + ", " + top_5_grouped_df['Pokeball']
        
        ax = top_5_grouped_df.plot(kind='bar', x='Pokemon Details', y='Successful Catches')

        # Make the x-axis labels horizontal and use 4 lines
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha='right', wrap=True)

        plt.show()
    else:
        print("No hay resultados exitosos para graficar.")
else:
    print("El DataFrame está vacío. No hay datos para graficar.")
# if not df.empty:
#     # Filtrar y agrupar los datos
#     filtered_df = df[df['Catch result'] == True]
#     grouped = filtered_df.groupby(['Pokemon', 'HP', 'Status Effect', 'Pokeball']).size()

#     # Verificar si el DataFrame agrupado está vacío
#     if not grouped.empty:
#         # Convertir el objeto groupby a un DataFrame
#         grouped_df = grouped.reset_index(name='Successful Catches')

#         # Plot the data
#         grouped_df.plot(kind='bar', x='Pokemon', y='Successful Catches')
#         plt.show()
#     else:
#         print("No hay resultados exitosos para graficar.")
# else:
#     print("El DataFrame está vacío. No hay datos para graficar.")
