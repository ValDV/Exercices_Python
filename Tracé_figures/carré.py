import matplotlib.pyplot as plt

def afficher_carre():
    x = [0, 3, 3, 0, 0]
    y = [0, 0, 3, 3, 0]

    plt.plot(x, y, marker='o')
    plt.fill(x, y, 'b', alpha=0.3)

    plt.axis('equal')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.show()

afficher_carre()
