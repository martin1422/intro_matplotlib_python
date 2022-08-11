# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

def scatter_plot(x, y):

    fig = plt.figure()
    fig.suptitle('Grafico', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)  # 1 fila, 2 columnas, axes nº1
    
    # Como los datos no están ordenados por año
    # el plot no funcionará bien en este caso
    ax1.scatter(x, y, c='darkgreen', label='Figuras')
    ax1.legend()
    ax1.grid()
    plt.show()
    print("Fin scatter plot")

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)

    # Alumno: Graficar la función utilizando "scatter"
    # utilizando "x" e "y" ya disponible

    # Colocar la leyenda y el label con el nombre de la función

    # Elegir un marker a elección

    # Crear acá su gráfico
    scatter_plot(x, y)

    print("terminamos")
