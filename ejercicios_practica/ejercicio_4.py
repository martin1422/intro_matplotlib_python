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


def cuatro_graficos(x, y1, y2, y3, y4):
    
    fig = plt.figure()
    fig.suptitle('Cuatro graficos', fontsize=16)
    ax1 = fig.add_subplot(2, 2, 1)  # 2 fila, 2 columnas, axes nº1
    ax2 = fig.add_subplot(2, 2, 2)  # 2 fila, 2 columnas, axes nº2    
    ax3 = fig.add_subplot(2, 2, 3)  # 2 fila, 2 columnas, axes nº3
    ax4 = fig.add_subplot(2, 2, 4)  # 2 fila, 2 columnas, axes nº4    

    ax1.plot(x, y1, c='r', marker='+')
    ax1.legend(['X^2'], title = "Cuadrado")
    ax1.grid()

    ax2.scatter(x, y2, c='c', marker='1')
    ax2.legend(['X^3'], title = "Cubo")
    ax2.grid(linestyle='dotted', linewidth=1)

    ax3.scatter(x, y3, c='y', marker='2')
    ax3.legend(['X^4'], title = "Cuarta")
    ax3.grid()
 
    ax4.scatter(x, y4, c='b', marker='3')
    ax4.legend(['X^(1/2)'], title = "Raiz")
    ax4.grid()

    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico
    cuatro_graficos(x, y1, y2, y3, y4)

    print("terminamos")
