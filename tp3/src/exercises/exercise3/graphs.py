import pandas as pd
import matplotlib.pyplot as plt

def exercise_3c():
    data = pd.read_csv('all_errors2.csv')
    iterations = data['Index']
    errors = data['Error']
    
    plt.plot(iterations, errors)
    plt.grid()
    plt.yticks(range(int(min(errors)), int(max(errors))+1, 1))
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.title('Error by Epoch in XOR Function')
    plt.show()

exercise_3c()