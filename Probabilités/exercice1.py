import random

def simuler_jet_de(nb_lancers):
    resultat = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(nb_lancers):
        face_obtenue = random.randint(1, 6)
        resultat[face_obtenue] += 1

    for face, count in resultat.items():
        probabilite = count / nb_lancers
        print(f"Face {face} : {count} fois ({probabilite * 100:.2f}%)")

simuler_jet_de(100)
