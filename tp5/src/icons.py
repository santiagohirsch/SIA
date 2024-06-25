import numpy as np

# Crear una matriz de 10x10 con valores de 1 y -1 para recrear una flecha a la derecha

import matplotlib.pyplot as plt
import numpy as np

# Define la matriz flecha_derecha
flecha_derecha = np.array([
    [1, 1, 1, 1, -1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, -1, -1, 1, 1, 1,1],
    [1, 1, 1, 1, -1, -1, -1, 1, 1, 1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, 1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1],
    [1, 1, 1, 1, -1, -1, -1, 1, 1, 1],
    [1, 1, 1, 1, -1, -1, 1, 1, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])
reloj_arena = np.array([
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, 1, 1, 1, 1, 1, 1, -1, -1],
    [1, -1, -1, 1, 1, 1, 1, -1, -1, 1],
    [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
    [1, 1, 1, -1, -1, -1, -1, 1, 1, 1],
    [1, 1, 1, -1, -1, -1, -1, 1, 1, 1],
    [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
    [1, -1, -1, 1, 1, 1, 1, -1, -1, 1],
    [-1, -1, 1, 1, 1, 1, 1, 1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
])


corazon = np.array([    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1, -1, -1,  1,  1, -1, -1,  1,  1],
    [ 1, -1, -1, -1, -1, -1, -1, -1, -1,  1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [ 1, -1, -1, -1, -1, -1, -1, -1, -1,  1],
    [ 1,  1, -1, -1, -1, -1, -1, -1,  1,  1],
    [ 1,  1,  1, -1, -1, -1, -1,  1,  1,  1],
    [ 1,  1,  1,  1, -1, -1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
])

rayo = np.array([
    [ 1,  1,  1,  1,  1,  1,  -1,  -1,  1,  1],
    [ 1,  1,  1,  1,  1,  -1,  -1,  1,  1,  1],
    [ 1,  1,  1,  1,  -1,  -1,  1,  1,  1,  1],
    [ 1,  1,  1,  -1,  -1,  1,  1,  1,  1,  1],
    [ 1,  1,  -1,  -1,  -1,  -1,  -1,  1,  1,  1],
    [ 1,  1,  1,  1,  -1,  -1,  1,  1,  1,  1],
    [ 1,  1,  1,  -1,  -1,  1,  1,  1,  1,  1],
    [ 1,  1,  -1,  -1,  1,  1,  1,  1,  1,  1],
    [ 1,  -1,  -1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1]
])

igual = np.array([
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [1, -1, -1, -1, -1, -1, -1, -1, -1, 1],
    [1, -1, -1, -1, -1, -1, -1, -1, -1, 1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [1, -1, -1, -1, -1, -1, -1, -1, -1, 1],
    [1, -1, -1, -1, -1, -1, -1, -1, -1, 1],
        [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1]
])

simbolo_division = np.array([
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  -1,  -1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  -1,  -1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [1, -1, -1, -1, -1, -1, -1, -1, -1, 1],
    [1, -1, -1, -1, -1, -1, -1, -1, -1, 1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  -1,  -1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  -1,  -1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1]
])

pause = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
    [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
    [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
    [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
    [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
    [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
    [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
    [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

podium = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, -1, -1, 1, 1, 1, 1],
    [1, 1, 1, -1, -1, -1, -1, 1, 1, 1],
    [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
    [1,-1, -1, 1, 1, 1, 1, -1, -1, 1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

smile = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, -1, -1, -1, 1, 1, -1, -1, -1, 1],
    [1, -1, -1, -1, 1, 1, -1, -1, -1, 1],
    [1, -1, -1, -1, 1, 1, -1, -1, -1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [-1, -1, 1, 1, 1, 1, 1, 1, -1, -1],
    [1, -1, -1, 1, 1, 1, 1, -1, -1, 1],
    [1, -1, -1, -1, -1, -1, -1, -1, -1, 1],
    [1, -1, -1, -1, -1, -1, -1, -1, -1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

square = np.array([
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
    [-1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
    [-1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
    [-1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
    [-1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
    [-1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
    [-1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
    [-1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
])

triangle = np.array([
    [ 1,  1,  1,  1,  1,  1,  1,  1,  -1, -1],
    [ 1,  1,  1,  1,  1,  1,  1,  -1, 1,  -1],
    [ 1,  1,  1,  1,  1,  1,  -1, 1,  1,  -1],
    [ 1,  1,  1,  1,  1,  -1, 1,  1,  1,  -1],
    [ 1,  1,  1,  1,  -1, 1,  1,  1,  1,  -1],
    [ 1,  1,  1,  -1, 1,  1,  1,  1,  1,  -1],
    [ 1,  1,  -1, 1,  1,  1,  1,  1,  1,  -1],
    [ 1,  -1, 1,  1,  1,  1,  1,  1,  1,  -1],
    [ -1, 1,  1,  1,  1,  1,  1,  1,  1,  -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
])

circle = np.array([
    [ 1,  1,  1, -1, -1, -1, -1,  1,  1,  1],
    [ 1,  1, -1,  1,  1,  1,  1, -1,  1,  1],
    [ 1, -1,  1,  1,  1,  1,  1,  1, -1,  1],
    [-1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
    [-1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
    [-1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
    [-1,  1,  1,  1,  1,  1,  1,  1,  1, -1],
    [ 1, -1,  1,  1,  1,  1,  1,  1, -1,  1],
    [ 1,  1, -1,  1,  1,  1,  1, -1,  1,  1],
    [ 1,  1,  1, -1, -1, -1, -1,  1,  1,  1],
])

rombo = np.array([
    [ 1,  1,  1,  1, -1,  1,  1,  1,  1,  1],
    [ 1,  1,  1, -1,  1, -1,  1,  1,  1,  1],
    [ 1,  1, -1,  1,  1,  1, -1,  1,  1,  1],
    [ 1, -1,  1,  1,  1,  1,  1, -1,  1,  1],
    [-1,  1,  1,  1,  1,  1,  1,  1, -1,  1],
    [ 1, -1,  1,  1,  1,  1,  1, -1,  1,  1],
    [ 1,  1, -1,  1,  1,  1, -1,  1,  1,  1],
    [ 1,  1,  1, -1,  1, -1,  1,  1,  1,  1],
    [ 1,  1,  1,  1, -1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
])

asterisk = np.array([
    [ -1,  1,  1,  1,  -1, -1,  1,  1,  1,  -1],
    [ 1,  -1,  1,  1,  -1, -1,  1,  1,  -1,  1],
    [ 1,  1,  -1,  1,  -1, -1,  1,  -1,  1,  1],
    [ 1,  1,  1,  -1,  -1, -1,  -1,  1,  1,  1],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [ 1,  1,  1,  -1,  -1, -1,  -1,  1,  1,  1],
    [ 1,  1,  -1,  1,  -1, -1,  1,  -1,  1,  1],
    [ 1,  -1,  1,  1,  -1, -1,  1,  1,  -1,  1],
    [-1,  1,  1,  1,  -1, -1,  1,  1,  1,  -1],
])

exclamation_mark = np.array([
    [ 1,  1,  1,  1, -1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1, -1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1, -1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1, -1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1, -1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  -1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  -1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1, -1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1, -1,  1,  1,  1,  1,  1],
])

question_mark = np.array([
    [ 1,  1,  1, -1, -1, -1, -1,  1,  1,  1],
    [ 1,  1, -1,  1,  1,  1, -1,  1,  1,  1],
    [ 1, -1,  1,  1,  1,  1, -1,  1,  1,  1],
    [ 1,  1,  1,  1,  1, -1,  1,  1,  1,  1],
    [ 1,  1,  1,  1, -1,  1,  1,  1,  1,  1],
    [ 1,  1,  1, -1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  -1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  -1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1, 1,  1, 1,  1,  1,  1,  1],
    [ 1,  1,  1, -1,  1, 1,  1,  1,  1,  1],
])

hashtag = np.array([
    [ 1,  1, -1,  1,  1, -1,  1,  1,  1,  1],
    [ 1,  1, -1,  1,  1, -1,  1,  1,  1,  1],
    [-1, -1, -1, -1, -1, -1, -1, -1,  1,  1],
    [ 1,  1, -1,  1,  1, -1,  1,  1,  1,  1],
    [ 1,  1, -1,  1,  1, -1,  1,  1,  1,  1],
    [-1, -1, -1, -1, -1, -1, -1, -1,  1,  1],
    [ 1,  1, -1,  1,  1, -1,  1,  1,  1,  1],
    [ 1,  1, -1,  1,  1, -1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
])

def get_icons():
    matrix_to_return = []
    matrix_to_return.append(flecha_derecha.flatten())
    matrix_to_return.append(reloj_arena.flatten())
    matrix_to_return.append(corazon.flatten())
    matrix_to_return.append(rayo.flatten())
    matrix_to_return.append(igual.flatten())
    matrix_to_return.append(simbolo_division.flatten())
    matrix_to_return.append(pause.flatten())
    matrix_to_return.append(podium.flatten())
    matrix_to_return.append(smile.flatten())
    matrix_to_return.append(square.flatten())
    matrix_to_return.append(triangle.flatten())
    matrix_to_return.append(circle.flatten())
    matrix_to_return.append(rombo.flatten())
    matrix_to_return.append(asterisk.flatten())
    matrix_to_return.append(exclamation_mark.flatten())
    matrix_to_return.append(question_mark.flatten())
    matrix_to_return.append(hashtag.flatten())
    matrix_to_return.append(flecha_izquierda.flatten())
    matrix_to_return.append(flecha_abajo.flatten())
    matrix_to_return.append(flecha_arriba.flatten())
    return matrix_to_return


flecha_izquierda = np.fliplr(flecha_derecha)
flecha_abajo = np.rot90(flecha_derecha, k=-1)
flecha_arriba = np.rot90(flecha_derecha, k=1)


# Visualiza la matriz usando matplotlib
# plt.subplot(4, 8, 1)
# plt.imshow(flecha_derecha, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Flecha Derecha')

# plt.subplot(4, 8, 2)
# plt.imshow(reloj_arena, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Reloj de Arena')

# plt.subplot(4, 8, 3)
# plt.imshow(corazon, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Corazón')

# plt.subplot(4, 8, 4)
# plt.imshow(rayo, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Rayo')

# plt.subplot(4, 8, 5)
# plt.imshow(igual, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Igual')

# plt.subplot(4, 8, 6)
# plt.imshow(simbolo_division, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('División')

# plt.subplot(4, 8, 7)
# plt.imshow(pause, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Pausa')

# plt.subplot(4, 8, 8)
# plt.imshow(podium, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Podium')

# plt.subplot(4, 8, 9)
# plt.imshow(smile, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Smile')

# plt.subplot(4, 8, 10)
# plt.imshow(square, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Square')

# plt.subplot(4, 8, 11)
# plt.imshow(triangle, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Triangle')

# plt.subplot(4, 8, 12)
# plt.imshow(circle, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Circle')

# plt.subplot(4, 8, 13)
# plt.imshow(rombo, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Rombo')

# plt.subplot(4, 8, 14)
# plt.imshow(asterisk, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Asterisk')

# plt.subplot(4, 8, 15)
# plt.imshow(exclamation_mark, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Exclamation Mark')

# plt.subplot(4, 8, 16)
# plt.imshow(question_mark, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Question Mark')

# plt.subplot(4, 8, 17)
# plt.imshow(hashtag, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Hashtag')

# plt.subplot(4, 8, 18)
# plt.imshow(flecha_izquierda, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Flecha Izquierda')

# plt.subplot(4, 8, 19)
# plt.imshow(flecha_abajo, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Flecha Abajo')

# plt.subplot(4, 8, 20)
# plt.imshow(flecha_arriba, cmap='gray', vmin=-1, vmax=1)
# plt.axis('off')
# plt.title('Flecha Arriba')

# plt.tight_layout()
# plt.show()
