import matplotlib.pyplot as plt
import pandas as pd

def plot_catches_by_hp(df):
    successful_catches = df[df["Catch result"] == True]
    
    hp_columns = pd.pivot_table(successful_catches, values='Catch result', index='Pokemon', columns='HP', aggfunc='count', fill_value=0)
    
    plt.figure(figsize=(10, 6))
    hp_columns.plot(kind='bar', stacked=True)
    
    plt.xlabel('Pokemon')
    plt.ylabel('Número de capturas exitosas')
    plt.title('Número de capturas exitosas por Pokemon y HP')
    plt.legend(title='HP')
    plt.xticks(rotation=45, ha='right')
    
    plt.show()

ruta_del_archivo = 'src/output/2b_results.csv'


df = pd.read_csv(ruta_del_archivo)
plot_catches_by_hp(df)
