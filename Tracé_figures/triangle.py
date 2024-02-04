import matplotlib.pyplot as plt
import numpy as np

def afficher_triangle():
    x = np.array([0, 1.5, 3])
    y = np.array([0, np.sqrt(3), 0])

    x = np.append(x, x[0])
    y = np.append(y, y[0])

    plt.plot(x, y, marker='o')
    plt.fill(x, y, 'b', alpha=0.3)

    plt.axis('equal')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.show()

afficher_triangle()
